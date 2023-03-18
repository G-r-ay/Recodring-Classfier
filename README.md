# The Recording-Classifier

The Recording-Classifier is a Python project that utilizes various machine learning techniques to analyze audio files for sentiment analysis. The system receives audio files, transcribes them using the AssemblyAI API, encodes the transcript using the Universal Sentence Encoder, and feeds it into a sentiment analysis model for classification.

## Getting Started
To run this project, clone the repository to your local machine and navigate to the project directory. Run the Main.py file, and the project will start capturing audio from your default audio input device. Once the audio capture is complete, the audio file is processed using the AssemblyAI API to convert the audio to text. Then, the text is encoded using the Universal Sentence Encoder, and the resulting embeddings are passed to a sentiment analysis model for classification.

## Usage
To use the Recording-Classifier, run the Main.py file. The project will start capturing audio from your default audio input device. Once the audio capture is complete, the audio file is processed using the AssemblyAI API to convert the audio to text. Then, the text is encoded using the Universal Sentence Encoder, and the resulting embeddings are passed to a sentiment analysis model for classification.

## Acknowledgments
This project was made possible by the AssemblyAI API and the Universal Sentence Encoder, developed by Google. We thank them for their contributions to the machine learning community.

### Conclusion
The Recording-Classifier project demonstrates the use of various machine learning techniques for sentiment analysis on audio files. By combining audio processing, natural language processing, and machine learning, we can gain insights into the emotional state of speakers and use that information to inform decision-making.
