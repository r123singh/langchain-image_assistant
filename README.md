# LangChain Image Assistant

LangChain Image Assistant is a console-based application that leverages LangChain and OpenAI's language models to analyze images and provide detailed insights.

## Features

- **Image Analysis**: Extracts and interprets textual information from images.
- **Console Interface**: Interact with the assistant directly through the command line.
- **AI-Powered**: Utilizes advanced language models for accurate and context-aware analysis.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/r123singh/langchain-image_assistant.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd langchain-image_assistant
   ```

3. **Set Up a Virtual Environment** (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your Image**: Ensure the image you want to analyze is accessible on your system.

2. **Run the Assistant**:

   ```bash
   python image-assistant.py --image_path /path/to/your/image.jpg
   ```

3. **Follow the Prompts**: The assistant will guide you through the analysis process, providing insights based on the image content.

## Configuration

The application uses `config.py` to manage settings such as API keys and model parameters. Ensure you have the necessary API keys for OpenAI configured in this file.

## Dependencies

- Python 3.8 or higher
- OpenAI API
- LangChain
- Other dependencies listed in `requirements.txt`

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the developers of LangChain and OpenAI for their powerful tools and APIs.
