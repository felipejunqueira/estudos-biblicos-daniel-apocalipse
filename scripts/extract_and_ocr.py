import subprocess
import os
import glob
import re
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = "/home/felipe/mycodes/estudos_biblicos"
DANIEL_PDF = os.path.join(BASE_DIR, "Estudo-Biblia-Facil-Daniel.pdf")
APOC_PDF = os.path.join(BASE_DIR, "Bíblia_Facil_Apocalipse.pdf")

DANIEL_IMG_DIR = os.path.join(BASE_DIR, "pages_daniel")
APOC_IMG_DIR = os.path.join(BASE_DIR, "pages_apocalipse")

DANIEL_OCR_DIR = os.path.join(BASE_DIR, "ocr_daniel")
APOC_OCR_DIR = os.path.join(BASE_DIR, "ocr_apocalipse")

for d in [DANIEL_IMG_DIR, APOC_IMG_DIR, DANIEL_OCR_DIR, APOC_OCR_DIR]:
    os.makedirs(d, exist_ok=True)

def render_page(args):
    pdf_path, page_num, out_prefix = args
    # pdftoppm single page
    cmd = ["pdftoppm", "-jpeg", "-r", "150", "-f", str(page_num), "-l", str(page_num), pdf_path, out_prefix]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return page_num

def run_ocr(args):
    img_path, txt_out_base = args
    cmd = ["tesseract", img_path, txt_out_base, "-l", "por", "--psm", "3"]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return img_path

def main():
    print("--- 1. Rendering Daniel pages (84 pages) ---")
    daniel_tasks = [
        (DANIEL_PDF, p, os.path.join(DANIEL_IMG_DIR, f"p_{p:03d}"))
        for p in range(1, 85)
    ]
    with ThreadPoolExecutor(max_workers=8) as executor:
        for p in executor.map(render_page, daniel_tasks):
            pass
    print("Done rendering Daniel.")

    print("--- 2. OCR Daniel pages ---")
    # find images
    daniel_imgs = sorted(glob.glob(os.path.join(DANIEL_IMG_DIR, "p_*.jpg")))
    ocr_tasks_daniel = []
    for img in daniel_imgs:
        base = os.path.splitext(os.path.basename(img))[0]
        out_base = os.path.join(DANIEL_OCR_DIR, base)
        ocr_tasks_daniel.append((img, out_base))
    
    with ThreadPoolExecutor(max_workers=8) as executor:
        for _ in executor.map(run_ocr, ocr_tasks_daniel):
            pass
    print("Done OCR Daniel.")

    print("--- 3. Rendering Apocalipse pages (101 pages) ---")
    apoc_tasks = [
        (APOC_PDF, p, os.path.join(APOC_IMG_DIR, f"p_{p:03d}"))
        for p in range(1, 102)
    ]
    with ThreadPoolExecutor(max_workers=8) as executor:
        for p in executor.map(render_page, apoc_tasks):
            pass
    print("Done rendering Apocalipse.")

    print("--- 4. OCR Apocalipse pages ---")
    apoc_imgs = sorted(glob.glob(os.path.join(APOC_IMG_DIR, "p_*.jpg")))
    ocr_tasks_apoc = []
    for img in apoc_imgs:
        base = os.path.splitext(os.path.basename(img))[0]
        out_base = os.path.join(APOC_OCR_DIR, base)
        ocr_tasks_apoc.append((img, out_base))

    with ThreadPoolExecutor(max_workers=8) as executor:
        for _ in executor.map(run_ocr, ocr_tasks_apoc):
            pass
    print("Done OCR Apocalipse.")

if __name__ == "__main__":
    main()
