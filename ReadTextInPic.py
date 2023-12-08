import cv2
import Text_Pic as tp
import TextToSpeech as ts
import os
from flask import Flask, render_template, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("myHome.html");

@app.route("/getText", methods=['GET'])
def getText():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()
    while True:
        # Capture a frame
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame in a window
        cv2.imshow("Camera", frame)
        cv2.imwrite("WebCamCapture.jpg", frame)
        text = tp.extract_text_from_image("WebCamCapture.jpg")
        #ts.text_to_speech(text)
        print(text)

        delete_file("WebCamCapture.jpg")

        break

    cap.release()
    cv2.destroyAllWindows()
    return jsonify({'text': text})


@app.route("/getAudio", methods = ['GET'])
def getAudio():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()
    while True:
        # Capture a frame
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame in a window
        cv2.imshow("Camera", frame)
        cv2.imwrite("WebCamCapture.jpg", frame)
        text = tp.extract_text_from_image("WebCamCapture.jpg")
        ts.text_to_speech(text)
        print(text)

        delete_file("WebCamCapture.jpg")

        break

    cap.release()
    cv2.destroyAllWindows()
    return send_file("output.mp3", as_attachment=False, mimetype='audio/mp3')




def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f'The file {file_path} has been deleted successfully.')
    except FileNotFoundError:
        print(f'The file {file_path} does not exist.')
    except Exception as e:
        print(f'An error occurred: {e}')

app.run(debug=True)

# Open a connection to the webcam (use 0 for the default camera)


# Check if the webcam is opened successfully


# Read and display frames from the webcam


    # Break the loop if 'q' key is pressed
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    # break

# Release the webcam and close the window

