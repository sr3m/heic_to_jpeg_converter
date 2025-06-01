# HEIC to JPEG converter

A lightweight Python script that scans its current folder for all `.heic` images, converts each one to `.jpeg` using Pillow (with HEIF support), and saves the results into a subfolder named `nueva_extension`. Simply place the `.py` file alongside your HEIC photos, open a Windows Command Prompt in that directory, and run the script.

Repository: [https://github.com/sr3m/heic\_to\_jpeg\_converter/tree/main](https://github.com/sr3m/heic_to_jpeg_converter/tree/main)

---

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [How It Works](#how-it-works)
* [Folder Structure](#folder-structure)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)

---

## Features

* **Bulk Conversion**: Automatically finds and converts all `.heic` files in the current directory.
* **Windows-Ready**: Uses Windows-style paths by default and is designed to be run from a Command Prompt.
* **Minimal Dependencies**: Relies on Pillow and `pillow_heif` for HEIC decoding.
* **Automatic Output Folder**: Creates a `nueva_extension` subfolder (if it doesn’t already exist) and places every converted `.jpeg` inside.
* **Simple Setup**: Just drop the script in your HEIC folder, install dependencies, and run.

---

## Prerequisites

* **Python 3.6+** installed on your Windows machine.
* A working **Command Prompt** (CMD) or **PowerShell**.
* The following Python packages:

  * [`Pillow`](https://pypi.org/project/Pillow/)
  * [`pillow_heif`](https://pypi.org/project/pillow-heif/)

---

## Installation

1. **Clone or Download**

   * Clone this repository or download `heic_to_jpeg.py` directly and place it in the folder containing your HEIC images:

   ```bash
   git clone https://github.com/sr3m/heic_to_jpeg_converter.git
   cd heic_to_jpeg_converter
   ```

2. **Create a Virtual Environment** (optional but recommended)

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```powershell
   pip install Pillow pillow_heif
   ```

   > **Note:**
   >
   > * `Pillow` is the Python Imaging Library used for opening, converting, and saving images.
   > * `pillow_heif` is a plugin that lets Pillow decode HEIC/HEIF files.

---

## Usage

1. **Place the Script**
   Copy (or move) `heic_to_jpeg.py` into the same directory that contains your `.heic` photo files.

2. **Open a Windows Command Prompt**
   Navigate (using `cd`) to the folder where both your HEIC images and the script live:

   ```powershell
   cd C:\path\to\your\heic\folder
   ```

3. **Run the Script**

   ```powershell
   python heic_to_jpeg.py
   ```

   * The script will:

     1. Check if a `nueva_extension` folder exists; if not, it creates it.
     2. Loop through every file in the current folder.
     3. For each file ending in `.heic`, open it, convert it to RGB, and save it as a `.jpeg` inside `nueva_extension`.
     4. Print how long the entire conversion took.

4. **Verify Output**

   * Once complete, open the `nueva_extension` folder.
   * You should see all of your original HEIC filenames but with a `.jpeg` extension—for example, `IMG_0001.heic` → `IMG_0001.jpeg`.

5. **Example Output**

   ```text
   Completed in 4.23 seg
   Thanks for using sr3m's image extractor algorithm
   ```

---

## How It Works

1. **Directory Listing**
   The script calls:

   ```python
   dir_list = os.listdir(os.getcwd())
   ```

   to get every filename in the current working directory.

2. **HEIC Plugin Registration**

   ```python
   register_heif_opener()
   ```

   allows Pillow’s `Image.open()` to decode `.heic` files.

3. **Folder Creation**

   ```python
   if not os.path.exists(".\\nueva_extension"):
       os.makedirs(".\\nueva_extension")
   ```

   ensures there is a folder named `nueva_extension`.

4. **File Loop & Conversion**

   ```python
   for i in dir_list:
       filename, extension_name = os.path.splitext(i)
       if extension_name.lower() == ".heic":
           src_path = os.path.join(os.getcwd(), i)
           dst_path = f".\\nueva_extension\\{filename}"
           with Image.open(src_path, mode="r") as im:
               im.convert("RGB").save(dst_path + ".jpeg", "JPEG")
   ```

   * Checks each file’s extension.
   * Opens the HEIC image, converts to RGB (required for JPEG), and saves it into `nueva_extension\{filename}.jpeg`.

5. **Timing**
   The script logs the start and finish times (using `time.time()`) to print how many seconds the batch took.

---

## Folder Structure

```
heic_to_jpeg_converter/
│
├─ heic_to_jpeg.py      # <-- Python script
├─ IMG_0001.heic
├─ IMG_0002.heic
├─ Holiday.heic
├─ other_file.txt
└─ ...
│
└─ nueva_extension/          # <-- Automatically created by the script
    ├─ IMG_0001.jpeg
    ├─ IMG_0002.jpeg
    ├─ Holiday.jpeg
    └─ ...
```

* **Root directory**: Contains `heic_to_jpeg.py` plus all your `.heic` images (and any other files).
* **`nueva_extension/` subfolder**: Populated automatically with the converted `.jpeg` files.

---

## Troubleshooting

* **“OSError: cannot identify image file”**

  * Ensure you installed `pillow_heif` correctly:

    ```powershell
    pip install pillow_heif
    ```
  * Make sure you ran `register_heif_opener()` before calling `Image.open(...)`.

* **Permission Denied / Access Errors**

  * Verify that you have read/write permissions in the target folder.
  * If files are open in another program, close them before running the script.

* **No HEIC Files Converted**

  * Double-check that your HEIC files truly have the extension `.heic` (all lowercase). The script checks `extension_name.lower() == ".heic"`.
  * Confirm you ran the script from the same folder where the HEIC files reside:

    ```powershell
    cd C:\path\to\your\heic\folder
    python heic_to_jpeg.py
    ```

* **Script Doesn’t Run at All**

  * Verify you’re using Python 3.x:

    ```powershell
    python --version
    ```
  * If `python` isn’t found, make sure Python is in your PATH, or try `py` instead:

    ```powershell
    py heic_to_jpeg.py
    ```

---

## Contributing

Contributions are welcome! If you’d like to:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a Pull Request.

Feel free to add enhancements, suggest bug fixes, or expand platform support (e.g., Linux/macOS path compatibility).

---

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). See the [LICENSE](LICENSE) file for details.
