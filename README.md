
# Python Poem Generator with Docker

## Description

This project is a Python-based interactive poem generator. It allows users to input some words and a theme to create a poem using the **Groq API**. The generated poem can be visualized as an image and played as audio.

### Features

- Generates poems with or without acrostic structure.
- Visualizes the generated poem as an image with a theme-based background.
- Converts the poem to speech and plays the audio.
- Dockerized for easy setup and execution.

---

## Prerequisites

Before running the application, ensure you have the following:

- **Docker** installed on your machine.

---

## How to Build and Run


### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-directory>
```
### Step 2: Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t pythone-poem-app .
```

### Step 3: Run the Docker Container

Run the following command to start the application:

```bash
docker run -it --rm pythone-poem-app
```

---

## Input and Output

### Inputs:

1. **Words**: Enter a phrase or words to inspire the poem.
2. **Theme**: Choose a theme (e.g., happiness, sadness, love).
3. **Acrostic Option**: Decide whether the poem should follow an acrostic structure (yes/no).

### Outputs:

- The poem will be displayed in the terminal.
- The poem will be saved as:
  - **Image**: `poem_visual.png`
  - **Audio**: `poem_audio.mp3`

---

## Directory Structure

```
.
├── Dockerfile          # Docker configuration
├── script.py           # Main Python script
├── requirements.txt    # Python dependencies
├── arial.ttf           # Font file (if needed)
└── README.md           # Project documentation
```

---

## Dependencies

The following Python libraries are used in the project:

- `groq`
- `gtts`
- `pillow`
- `numpy`
- `matplotlib`

--- 
## Known Issues and Solutions

1. **Font Not Found**:

   - Ensure `arial.ttf` is placed in the same directory as `Dockerfile`.
   - Alternatively, use a default font by modifying the script.

3. **Groq API Key**:

   - Replace the placeholder API key in the script with a valid Groq API key.

4. **Docker Build Issues**:

   - On some systems, limited resources (like low memory) can cause Docker build failures. Ensure adequate resources are allocated to Docker.

5. **Interactive Input in Docker**:

   - If running the container interactively fails, ensure the `-it` flag is used with `docker run`.

6. **Audio Not Playing Automatically**:

   - Depending on the system, `os.system("start")` might not work. Ensure your system supports the current approach or consider replacing it with other platform-specific solutions if needed.

---

## Problems and solutions received during development

- When uploading files with scp, I was always using the ssh key reference, so I was getting permission denied because of a difference in structure, but I found the correct upload order by experimenting and uploaded it.

- While writing the script, finding the right prompts to get the output we want can be considered a problem with a lot of trial and error.

## Author

Developed by Emrehan ÇETİN. Feel free to contribute or report issues!