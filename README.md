# Image to ASCII Art Generator

![ASCII Art Generator Banner]

A simple yet engaging web application built with Django that converts uploaded images into ASCII art. This project demonstrates basic file handling, image processing with Pillow, and dynamic content rendering using Django templates and Tailwind CSS for a modern dark-mode aesthetic.

## Features

* **Image Upload:** Easily upload images through a user-friendly interface.
* **ASCII Conversion:** Converts uploaded images into ASCII text art.
* **Dynamic Resizing:** Adjusts ASCII output width based on the original image's width (1:3 ratio) while correcting aspect ratio for proper display.
* **Dark Mode UI:** Modern and sleek user interface styled with Tailwind CSS in a dark theme.
* **Ephemeral Results:** Uploaded images and their ASCII art results are cleared upon page refresh, maintaining a clean state.

## Technologies Used

* **Backend:** Python 3.x, Django
* **Image Processing:** Pillow
* **Frontend:** HTML, Tailwind CSS
* **Database:** SQLite (default for development)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed on your system:

* [Python 3.8+](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)
* [Git](https://git-scm.com/downloads) (for cloning the repository)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/Hailrn/ascii_art_project.git](https://github.com/USERNAME_ANDA/NAMA_REPO_ANDA.git)
    cd NAMA_REPO_ANDA # Ganti dengan nama repository Anda
    ```

2.  **Create a virtual environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install project dependencies:**
    All required Python packages are listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

5.  **Create necessary directories:**
    The application requires a `media` directory to temporarily store uploaded images.

    ```bash
    mkdir media
    ```

6.  **Run database migrations:**
    This sets up the necessary database tables for the Django project, including the session table.

    ```bash
    python manage.py migrate
    ```

### Running the Application

1.  **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.
