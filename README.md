# Math-me-Up

### By Abel Simon and Athul Sanjose

Mathematics is fundamental for many professions, especially science, technology, and engineering. Yet, mathematics is often perceived as difficult by most students. Studying math through e-learning medium and physical interactive medium can supplement the traditional textbook learning, and so we came up with the idea of Math-me-Up. It provides a Web-App with a collection of mathematical problems of various levels of difficulty from different branches of mathematics. An IoT-based device helps the user to solve these problems within the recommended time limit of each question, thereby improving their cognitive and mathematical-problem solving capabilities. The user also has the option to contribute questions for the greater good and help other students in search of questions for a particular topic. 

<br/>

We have also built an Arduino-based device which helps the user understand the binary number system and the conversions between various number systems in an interactive and fun manner.

## Setup Math-me-Up

### Hardware setup

- The list of required hardware components are given in [components](Arduino/Components.csv).
- Connnect the components according to the circuit shown below at a convenient location and connect to power.

 <br />
 
![circuit](Arduino/Circuit-Diagram.png?raw=true)

<br/>

- Upload the [code](Arduino/math_me_up1.ino) onto your Arduino Uno.

### Clone the repo

```
$ git clone https://github.com/abelzach/Math-me-Up
$ cd Math-me-Up
```

### Install dependencies

```
$ cd Web-App
$ pip install -r requirements.txt
```
### Run the Web-App

```
$ python app.py
```

- Visit locahost:5000 in your web browser and enjoy the Math-me-Up experience.
