import zipfile, tempfile, os, json, subprocess, re

def extract_zip(path):
    d = tempfile.mkdtemp()
    with zipfile.ZipFile(path,'r') as z:
        z.extractall(d)
    return d

def find_py_files(root):
    out=[]
    for r,_,files in os.walk(root):
        for f in files:
            if f.endswith('.py'):
                out.append(os.path.join(r,f))
    return out

def check_syntax(pyfile):
    try:
        subprocess.check_output(['python3','-m','py_compile', pyfile], stderr=subprocess.STDOUT)
        return True, ""
    except subprocess.CalledProcessError as e:
        return False, e.output.decode()

def ros_structure_check(root):
    found_pkg = False
    for r,_,files in os.walk(root):
        for f in files:
            if f in ['package.xml','CMakeLists.txt','setup.py']:
                found_pkg = True
    return found_pkg

def detect_basic_ros_calls(pyfile):
    txt = open(pyfile,'r',errors='ignore').read()
    return {
        "has_init": "rclpy.init" in txt or "rospy.init_node" in txt,
        "pubs": len(re.findall(r"Publisher|create_publisher", txt)),
        "subs": len(re.findall(r"Subscriber|create_subscription", txt)),
    }

def run_checks(zip_path):
    root = extract_zip(zip_path)
    pyfiles = find_py_files(root)

    report = {"status":"FAILED","syntax_errors":[], "structure_valid": False, "node_info": {}}

    report["structure_valid"] = ros_structure_check(root)

    for p in pyfiles:
        ok,err = check_syntax(p)
        if not ok:
            report["syntax_errors"].append({"file":p,"err":err})

    if pyfiles:
        report["node_info"] = detect_basic_ros_calls(pyfiles[0])

    if report["structure_valid"] and not report["syntax_errors"]:
        report["status"] = "PASSED"

    with open('report.json','w') as f:
        json.dump(report,f,indent=2)

    return report

if __name__=='__main__':
    import sys
    print(run_checks(sys.argv[1]))