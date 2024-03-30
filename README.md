<!DOCTYPE html>
<html lang="en">

<body>

<h1>Quizzler App</h1>

<h2>Overview:</h2>
<p>Quizzler App is a simple interactive quiz game where users can answer true/false questions and test their knowledge on various topics. The app fetches questions from an online API and presents them to the user in a user-friendly graphical interface. The question set can be customized by changing the API key.</p>

<h2>Features:</h2>
<ol>
    <li>True/false questions fetched from an online API.</li>
    <li>User-friendly graphical interface using Tkinter library.</li>
    <li>Score tracking to keep track of user performance.</li>
    <li>Color-coded feedback for correct and incorrect answers.</li>
    <li>Simple and intuitive navigation with true/false buttons.</li>
    <li>Customizable question set by changing the API key in the data.py file.</li>
    <li>Developed using the Tkinter library for creating the GUI.</li>
</ol>

<h2>Installation:</h2>
<ol>
    <li>Clone the repository to your local machine:
        <code>git clone https://github.com/Manjunathhs-0003/Quizzler-App.git</code></li>
    <li>Navigate to the project directory:
        <code>cd Quizzler-App</code></li>
    <li>Set the question set API:
        <ul>
          <li>Open Trivia is a platform that provides a vast collection of trivia questions across various categories. Users can access trivia questions for free, covering topics such as general knowledge, sports, entertainment, history, and more.</li>
            <li>Visit <a href="https://opentdb.com/api_config.php">Open Trivia Database API Configuration</a></li>
            <li>Obtain an API key and replace it in the data.py file.</li>
            <li>API key allows customization of the question set.</li>
        </ul></li>
    <li>Run the application:
        <code>python main.py</code></li>
</ol>

<h2>Usage:</h2>
<ul>
    <li>Upon running the application, the user is presented with a series of true/false questions.</li>
    <li>Click the "True" or "False" buttons to answer the question.</li>
    <li>Receive color-coded feedback for correct and incorrect answers.</li>
    <li>View the score displayed on the top.</li>
    <li>Continue answering questions until reaching the end of the quiz.</li>
</ul>

</body>
</html>
