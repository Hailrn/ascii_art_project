from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from PIL import Image
import os
import io

def process_image_to_ascii(image_path_or_file):
    try:
        if isinstance(image_path_or_file, str):
            img = Image.open(image_path_or_file)
        else:
            img = Image.open(image_path_or_file)
        
        img = img.convert("L")

        original_width, original_height = img.size
        output_width = original_width // 8 #1:8

        if output_width == 0:
            output_width = 1

        aspect_ratio = original_height / original_width
        output_height = int(output_width * aspect_ratio * 0.55) 
        
        if output_height == 0:
            output_height = 1

        img = img.resize((output_width, output_height))

        ASCII_CHARS = "@%#*+=-:. " 
        
        pixels = img.getdata()
        ascii_str = ""
        for pixel_value in pixels:
            index = int((pixel_value / 255) * (len(ASCII_CHARS) - 1))
            ascii_str += ASCII_CHARS[index]
        
        ascii_art = ""
        for i in range(0, len(ascii_str), output_width):
            ascii_art += ascii_str[i:i+output_width] + "\n"
        
        return ascii_art

    except Exception as e:
        print(f"Error saat memproses gambar: {e}")
        return None

def upload_image_view(request):
    ascii_art_result = None
    uploaded_image_url = None

    if request.method == 'POST' and request.FILES.get('image_file'):
        uploaded_file = request.FILES['image_file']
        
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = os.path.join(fs.location, filename)

        ascii_art_result = process_image_to_ascii(file_path)
        
        # Hapus file gambar setelah selesai diproses
        # try:
        #     fs.delete(filename)
        # except Exception as e:
        #     print(f"Gagal menghapus file '{filename}': {e}") 
        
        if not ascii_art_result:
            # error handling
            request.session['ascii_result'] = "Gagal mengkonversi gambar. Coba gambar lain ya!"
            request.session['uploaded_img_url'] = None
        else:
            request.session['ascii_result'] = ascii_art_result
            request.session['uploaded_img_url'] = "media/" + filename

        return redirect('upload_image') # url name in urls.py

    # GET request (termasuk redirect)
    ascii_art_result = request.session.pop('ascii_result', None)
    uploaded_image_url = request.session.pop('uploaded_img_url', None)

    # Render template HTML
    return render(request, 'ascii_converter/upload.html', {
        'ascii_art': ascii_art_result,
        'uploaded_image_url': uploaded_image_url,
    })