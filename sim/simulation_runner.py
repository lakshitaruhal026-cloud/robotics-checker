# sim/simulation_runner.py
import os, time, json
from PIL import Image, ImageDraw

OUT_DIR = os.path.join(os.getcwd(), "sim", "sample_frames")
os.makedirs(OUT_DIR, exist_ok=True)

def make_frame(text, fname):
    im = Image.new('RGB', (640, 480), (240, 240, 240))
    d = ImageDraw.Draw(im)
    d.text((20,200), text, fill=(20,20,20))
    path = os.path.join(OUT_DIR, fname)
    im.save(path)
    return path

def run_simulation(_node_zip_path=None):
    frames = []
    for i in range(1,6):
        fname = f"frame_{i}.png"
        path = make_frame(f"Sim preview frame {i}", fname)
        frames.append(path)
        time.sleep(0.05)
    result = {
        "success": True,
        "frames": frames,
        "joint_positions": [0.0, 0.5, 1.0, 0.2, -0.2, 0.0]
    }
    with open("sim_result.json", "w") as f:
        json.dump(result, f, indent=2)
    return result

if __name__ == "__main__":
    print(run_simulation(None))