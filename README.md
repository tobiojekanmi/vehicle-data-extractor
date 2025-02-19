# Vehicle Details Extraction from Images using AI

This project is designed to extract detailed information about vehicles from images using an AI model. The AI analyzes the image and provides structured data such as the vehicle type, license plate number, make, model, and color. The project leverages the **Ollama API** for AI inference and is built using Python.

---

## Technology Stack

- **Python**: The script is written in Python, leveraging libraries like `argparse` for command-line argument parsing and `json` for structuring and validating model output.
- **Ollama**: The project uses the Ollama API, which provides a powerful AI model capable of analyzing images and extracting structured data. The model used in this project is `llama3.2-vision:latest`, which is optimized for vision-based tasks.

---

## Information Extraction Pipeline

1. **Input**: The user provides an image file containing a vehicle.
2. **Preprocessing**: The image is passed directly to the Ollama API without additional preprocessing.
3. **AI Inference**: The Ollama API analyzes the image and extracts vehicle details based on the provided prompts.
4. **Output**: The AI returns a JSON object containing the extracted details, such as vehicle type, license plate, make, model, and color.
5. **Validation**: The output is validated against a predefined JSON schema to ensure it meets the required structure.

---

## How to Use the Code

### Prerequisites

1. **Python**: Ensure Python 3.x is installed on your system.
2. **Ollama API**: The Ollama API must be running locally at `http://localhost:11434`. To install Ollama and start the `llama3.2-vision:latest` model, follow the steps provided at (https://ollama.com/)[https://ollama.com/].

### Steps to Run the Code

1. **Clone the Repository**:

```
git clone https://github.com/your-repo/vehicle-details-extraction.git
cd vehicle-details-extraction
```

2. **Run the Script**:
   Use the following command to execute the script, providing the path to the image file:

```
python main.py -p /path/to/your/image.jpg
```

Kindly note that the `main.py` file accepts the following command-line arguments:

```
-p or --path: The path to the image file (required).
```

3. **View the Output**:
   The script will output a JSON object containing the extracted vehicle details. For example:

```
{
    "Type": "Car",
    "License": "ABC123",
    "Make": "Toyota",
    "Model": "Corolla",
    "Color": "Red"
}
```

---

## Limitations

- The accuracy of the results depends on the quality of the input image and the capabilities of the AI model. The AI may not detect details if the image is blurry, poorly lit, or the vehicle is partially obscured.

- The script currently supports only local image files.

---

## Possible Future Enhancements

- Add support for batch processing of multiple images.

- Integrate with cloud-based APIs for scalability.

- Add a user-friendly interface (e.g., a web app or GUI).
