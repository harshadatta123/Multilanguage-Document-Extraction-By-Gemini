
# Multilanguage Document Extraction by Gemini

## Documentation

### Code Explained

This project, Multilanguage Document Extraction by Gemini, leverages the Google Gemini Pro Vision API to extract vital information from multilingual documents. The application is built using Streamlit for the web interface and utilizes environmental variables for secure API key management. The following steps were used in the making of this project:

#### Environment Setup

The code begins with loading environment variables using the `dotenv` library to securely manage sensitive information such as API keys. This ensures that the Google API key is not hard-coded into the script but instead retrieved from a secure `.env` file.

![image](https://github.com/user-attachments/assets/8e26a5b8-b147-4859-8d9f-b9c194baf928)


#### Streamlit Initialization

Streamlit is used to create a user-friendly web interface. The app is initialized with a title and header providing a clear and concise introduction to the application.

![image](https://github.com/user-attachments/assets/d5ede5d2-3914-4049-9745-332252501cc7)

#### Description Text

A descriptive text is added to inform the users about the purpose of the application. The text is styled using Markdown for better presentation.
![image](https://github.com/user-attachments/assets/5ce37b40-8cd8-4358-bca1-1e57c34d5c1c)


#### Google Gemini Pro Vision API Function

The core functionality of the application is to communicate with the Google Gemini Pro Vision API. The function `get_gemini_response` initializes the API model and sends the multimodal prompt (which includes the uploaded image and user input) to the API, returning the extracted information.

![image](https://github.com/user-attachments/assets/1dbfd35f-debd-4d77-96f4-74f16834dbad)

#### Image Upload Setup

The application allows users to upload images of documents. The `input_image_setup` function opens the uploaded image using the Pillow library (PIL), ensuring the image is correctly processed.

![image](https://github.com/user-attachments/assets/a4f524ef-b65c-41e2-a9d6-d689fd0bd672)

#### User Input for Prompt

The application provides a text input field for users to enter their prompt. This prompt, along with the uploaded image, forms the multimodal input that is sent to the Google Gemini Pro Vision API.

![image](https://github.com/user-attachments/assets/87fa288e-3b13-4fce-8710-34927ac5ad48)

In summary, this project built with Streamlit and Google Gemini Pro Vision API offers a seamless experience for extracting information from multilingual documents. The app ensures data security through environment variables and provides a user-friendly interface for uploading images and entering prompts. The extracted information is displayed efficiently, enhancing productivity and decision-making processes.

### Conclusion

The Multilanguage Document Extraction by Gemini project has successfully demonstrated the capability to extract vital information from diverse multilingual documents using the Google Gemini Pro Vision API. The integration of Streamlit has provided a user-friendly interface that allows users to effortlessly upload documents and view the extracted content. The application has been tested extensively and has performed well with most test cases, showcasing its efficiency and accuracy in handling various document types and languages.

Key features such as context-aware content extraction, robust security measures, and scalability have been effectively implemented, ensuring that the application meets the needs of a wide range of users. The project has achieved its primary objectives of enhancing productivity, transcending language barriers, and enabling data-driven decision-making.

Overall, this project stands as a powerful tool for organizations and individuals dealing with multilingual documents, providing a reliable and efficient solution for extracting and managing critical information.
```
