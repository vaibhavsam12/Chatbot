import random
import cv2

# List of songs
songs = [
  "Bohemian Rhapsody by Queen",
  "Stairway to Heaven by Led Zeppelin",
  "Smells Like Teen Spirit by Nirvana",
  "Imagine by John Lennon",
  "Hotel California by Eagles"
]

# Function to suggest a random song
def suggest_song():
  return random.choice(songs)

# Function to display the suggested song
def display_suggestion():
  suggestion = suggest_song()
  print("Sure, here's a song you might like: " + suggestion)

# Ask the user if they want a song suggestion
want_suggestion = input("Do you want a song suggestion? (yes/no)")

# If the user wants a song suggestion, ask them to upload an image for face recognition
if want_suggestion.lower() == "yes":
  # Load the face recognition model
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

  # Ask the user to upload an image
  image = input("Please upload an image: ")

  # Read the image
  img = cv2.imread(image)

  # Convert the image to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Detect faces in the image
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

  # If a face is detected, suggest a song based on the user's identity
  if len(faces) > 0:
    display_suggestion()
  else:
    print("No face was detected in the image.")
else:
  print("Okay, maybe later.")