import os
import pandas as pd
from datasets import load_dataset
from tqdm import tqdm
import json

dataset = load_dataset(f"WaltonFuture/Multimodal-Cold-Start", split="train")

image_folder = f"data/Multimodal-Cold-Start/images"
json_path = f"data/Multimodal-Cold-Start.json"
os.makedirs(image_folder, exist_ok=True)  

converted_data = []
for i, da in tqdm(enumerate(dataset)):
    json_data = {}
    json_data["query"] = da["problem"]
    json_data["response"] = da["answer"]
    imgpath = os.path.join(image_folder, f"{i}.jpg")
    json_data["images"] = [imgpath]
    da["images"][0].convert("RGB").save(imgpath)
    converted_data.append(json_data)

with open(json_path, "w") as f:
    json.dump(converted_data, f, indent=4, ensure_ascii=False)
