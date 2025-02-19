import os
import json
import argparse
from ollama import chat


# System Prompt - Defines assistant behavior
system_prompt = """
You are an AI assistant specializing in extracting vehicle details from images. 
Your task is to inspect the given image and provide accurate details about the vehicle.
If a specific detail is unclear or not well detected, return `None` for that field.
Do not make guesses or assumptions.
"""

# JSON Output Format Schema
output_format = {
    "type": "object",
    "properties": {
        "Type": {
            "title": "Vehicle Type",
            "description": "The type of vehicle detected in the image.",
            "examples": ["Car", "Truck", "Motorcycle", "Bus", "Van"],
            "type": ["string", "null"],
        },
        "License": {
            "title": "License Plate",
            "description": "The vehicle's license plate number.",
            "type": ["string", "null"],
        },
        "Make": {
            "title": "Make",
            "description": "The brand or manufacturer of the vehicle.",
            "examples": ["Toyota", "Honda", "Ford", "Suzuki"],
            "type": ["string", "null"],
        },
        "Model": {
            "title": "Model",
            "description": "The specific model of the vehicle.",
            "examples": ["Corolla", "Civic", "F-150"],
            "type": ["string", "null"],
        },
        "Color": {
            "title": "Color",
            "description": "The primary color of the vehicle.",
            "examples": ["Red", "Blue", "Black", "White"],
            "type": ["string", "null"],
        },
    },
    "required": ["Type", "License", "Make", "Model", "Color"],
}

# User Prompt - Directs the AI on expected output
user_prompt = f"""
Analyze the image and extract the following details about the vehicle:
- Vehicle Type
- License Plate Number
- Make (Brand)
- Model
- Color

The response must be a JSON object that strictly conforms to the schema below:
```json
{json.dumps(output_format, indent=4)}
```
If any detail is unclear or unreadable, return null for that field.
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract vehicle information from an image using AI."
    )
    parser.add_argument("-p", "--path", required=True, help="Path to the image file")
    args = parser.parse_args()

    # Validate image path
    if not os.path.isfile(args.path):
        print(f"Error: The file {args.path} does not exist or is not readable.")
        exit(1)

    # Extract vehicle data from the given image
    response = chat(
        model="llama3.2-vision:latest",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt, "images": [args.path]},
        ],
        format="json",
        options={"temperature": 0},
    )

    # Print result to stdout
    try:
        output = json.loads(response["message"]["content"])
        print("Image: ", args.path)
        print("Description: \n", json.dumps(output, indent=4))
        print("")
    except (KeyError, json.JSONDecodeError) as e:
        raise ValueError(
            "Invalid response format: Expected a valid JSON output."
        ) from e
