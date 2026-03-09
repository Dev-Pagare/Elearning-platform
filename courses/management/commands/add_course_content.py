from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, Lesson

COURSE_CONTENT = {
    "Python Programming": [
        {
            "title": "Introduction to Python", "order": 1,
            "lessons": [
                {
                    "title": "What is Python?", "order": 1,
                    "content": """Python is a high-level, interpreted programming language known for its simplicity and readability.

It was created by Guido van Rossum and first released in 1991.

Why Learn Python?
- Clean and readable syntax that feels like writing English
- Beginner-friendly with a short learning curve
- Versatile — used in Web, AI, Data Science, Automation
- Huge community and library support

Where is Python Used?
- Web Development (Django, Flask)
- Data Science and Machine Learning (Pandas, TensorFlow)
- Automation and Scripting
- Cybersecurity and Ethical Hacking
- Game Development""",
                    "code": """# Your first Python program
print("Hello, World!")

# Check Python version
import sys
print(sys.version)

# Python is easy to read
name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")"""
                },
                {
                    "title": "Setting Up Python Environment", "order": 2,
                    "content": """Step 1 — Install Python:
- Go to python.org
- Click Downloads and choose the latest version
- Run the installer
- Important: Check "Add Python to PATH" before installing
- Click Install Now

Step 2 — Install VS Code:
- Go to code.visualstudio.com
- Download and install VS Code
- Open VS Code Extensions (Ctrl+Shift+X)
- Search "Python" and install the Microsoft Python extension

Step 3 — Write Your First Program:
- Open VS Code
- Create a new file and save as hello.py
- Type your code
- Press F5 or right-click and Run Python File""",
                    "code": """# Verify Python is installed in terminal:
# python --version

# hello.py
print("Python is ready!")

# Simple calculator
a = 10
b = 5
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)"""
                }
            ]
        },
        {
            "title": "Variables and Data Types", "order": 2,
            "lessons": [
                {
                    "title": "Variables in Python", "order": 1,
                    "content": """A variable is a container that stores data values.

In Python, you do not need to declare a variable type — Python figures it out automatically.

Variable Naming Rules:
- Must start with a letter or underscore (_)
- Cannot start with a number
- Can only contain letters, numbers, and underscores
- Case-sensitive (name and Name are different variables)
- Cannot use Python reserved keywords (if, for, while, etc.)

Best Practices:
- Use descriptive names (student_name not sn)
- Use snake_case for multiple words
- Keep names short but meaningful""",
                    "code": """# Creating variables
name = "John"
age = 25
height = 5.11
is_student = True

# Print variables
print(name)         # John
print(age)          # 25
print(height)       # 5.11
print(is_student)   # True

# Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)      # 10 20 30

# Same value to multiple variables
a = b = c = 100
print(a, b, c)      # 100 100 100"""
                },
                {
                    "title": "Data Types", "order": 2,
                    "content": """Python has several built-in data types:

1. int — Whole numbers: 10, -5, 0, 1000
2. float — Decimal numbers: 3.14, -2.5, 0.001
3. str — Text: "Hello", "Python", "123"
4. bool — True or False
5. list — Ordered changeable collection: [1, 2, 3]
6. tuple — Ordered unchangeable collection: (1, 2, 3)
7. dict — Key-value pairs: {"name": "John", "age": 25}
8. set — Unordered unique items: {1, 2, 3}

Use type() function to check the data type of any variable.""",
                    "code": """# Integer
age = 25
print(type(age))          # <class 'int'>

# Float
pi = 3.14159
print(type(pi))           # <class 'float'>

# String
name = "Python"
print(type(name))         # <class 'str'>

# Boolean
is_active = True
print(type(is_active))    # <class 'bool'>

# List
fruits = ["apple", "banana", "cherry"]
print(fruits[0])          # apple

# Dictionary
student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])    # John

# Type conversion
x = "100"
y = int(x)                # String to int
print(y + 50)             # 150"""
                }
            ]
        },
        {
            "title": "Control Flow", "order": 3,
            "lessons": [
                {
                    "title": "If-Else Statements", "order": 1,
                    "content": """Control flow allows your program to make decisions based on conditions.

if statement — executes code only if condition is True
elif — checks another condition if the previous was False
else — executes when all conditions are False

Comparison Operators:
== (equal to)
!= (not equal to)
>  (greater than)
<  (less than)
>= (greater than or equal to)
<= (less than or equal to)

Logical Operators:
and — both conditions must be True
or  — at least one condition must be True
not — reverses the condition""",
                    "code": """# Basic if-else
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# if-elif-else
marks = 75
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"
print(f"Your grade is: {grade}")  # B

# Logical operators
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials!")"""
                },
                {
                    "title": "Loops in Python", "order": 2,
                    "content": """Loops allow you to execute a block of code multiple times.

Two types of loops in Python:
1. for loop — iterates over a sequence (list, string, range)
2. while loop — repeats as long as condition is True

Loop Control Statements:
- break — exits the loop immediately
- continue — skips the current iteration
- pass — does nothing (placeholder)

range() function:
- range(5) gives 0, 1, 2, 3, 4
- range(1, 6) gives 1, 2, 3, 4, 5
- range(0, 10, 2) gives 0, 2, 4, 6, 8""",
                    "code": """# for loop
for i in range(5):
    print(i)   # 0 1 2 3 4

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while loop
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# break example
for i in range(10):
    if i == 5:
        break
    print(i)   # 0 1 2 3 4

# continue — skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)   # 1 3 5 7 9"""
                }
            ]
        },
        {
            "title": "Functions", "order": 4,
            "lessons": [
                {
                    "title": "Defining and Calling Functions", "order": 1,
                    "content": """A function is a block of reusable code that performs a specific task.

Why use functions?
- Avoid repeating code (DRY — Don't Repeat Yourself)
- Make code organized and readable
- Easy to test and debug

Types of functions:
1. Built-in functions — print(), len(), type(), input()
2. User-defined functions — functions you create yourself
3. Lambda functions — small anonymous functions

Function components:
- def keyword — defines the function
- Function name — identifier to call it
- Parameters — input values (optional)
- Docstring — description (optional but recommended)
- Return statement — output value (optional)""",
                    "code": """# Basic function
def greet():
    print("Hello, Welcome!")

greet()   # Hello, Welcome!

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")   # Hello, Alice!

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # 8

# Default parameter values
def greet(name, message="Good morning"):
    print(f"{message}, {name}!")

greet("John")              # Good morning, John!
greet("Alice", "Hi")       # Hi, Alice!

# Lambda function
square = lambda x: x ** 2
print(square(5))   # 25"""
                }
            ]
        }
    ],

    "Video Editing": [
        {
            "title": "Introduction to Video Editing", "order": 1,
            "lessons": [
                {
                    "title": "What is Video Editing?", "order": 1,
                    "content": """Video editing is the process of manipulating and rearranging video shots to create a final video product.

Video editing involves:
- Cutting and trimming footage
- Adding transitions between clips
- Color grading and correction
- Adding music and sound effects
- Adding text, titles, and graphics
- Exporting the final video

Popular Video Editing Software:
1. Adobe Premiere Pro — Industry standard, professional
2. DaVinci Resolve — Free, powerful color grading
3. Final Cut Pro — Apple exclusive, fast performance
4. CapCut — Free, beginner-friendly
5. Filmora — Easy to use, good for beginners

Career Opportunities:
- YouTube Content Creator
- Film and TV Editor
- Social Media Video Editor
- Corporate Video Producer
- Wedding Videographer""",
                    "code": ""
                },
                {
                    "title": "Understanding the Timeline", "order": 2,
                    "content": """The Timeline is the core of any video editing software.

Timeline Components:
1. Video Tracks (V1, V2, V3) — Layer your video clips
2. Audio Tracks (A1, A2, A3) — Layer your audio
3. Playhead — Shows your current position
4. In and Out Points — Mark clip start and end
5. Time Ruler — Shows time in hours:minutes:seconds:frames

Key Timeline Operations:
- Drag and drop clips onto the timeline
- Trim clips by dragging edges
- Split clips using the razor/blade tool
- Move clips by dragging
- Lock tracks to prevent accidental edits

Important Keyboard Shortcuts (Premiere Pro):
- Spacebar — Play/Pause
- C — Razor/Cut tool
- V — Selection tool
- Ctrl+Z — Undo
- Ctrl+S — Save project""",
                    "code": ""
                }
            ]
        },
        {
            "title": "Cutting and Trimming", "order": 2,
            "lessons": [
                {
                    "title": "Basic Cuts and Transitions", "order": 1,
                    "content": """Cuts are the most fundamental editing technique.

Types of Cuts:
1. Hard Cut — Instant switch from one clip to another
2. Jump Cut — Cuts between two similar shots (same subject, different angles)
3. Match Cut — Cuts on a similar action or visual element
4. L-Cut — Audio from clip A continues into clip B
5. J-Cut — Audio from clip B starts before the video

Types of Transitions:
1. Dissolve — Gradual blend between two clips
2. Wipe — One clip pushes the other off screen
3. Fade to Black — Clip fades to black
4. Zoom Transition — Zoom in or out between clips

Best Practices:
- Use transitions sparingly
- Hard cuts work best for most situations
- Match the energy of your transitions to your content
- Keep transitions consistent throughout the video""",
                    "code": ""
                }
            ]
        },
        {
            "title": "Color Grading", "order": 3,
            "lessons": [
                {
                    "title": "Color Correction Basics", "order": 1,
                    "content": """Color correction ensures your footage looks natural and consistent.

Color Correction Steps:
1. Exposure — Adjust brightness (not too bright or dark)
2. White Balance — Fix color temperature (warm or cool)
3. Contrast — Difference between bright and dark areas
4. Highlights — Bright areas of the image
5. Shadows — Dark areas of the image
6. Saturation — Intensity of colors

Color Grading vs Color Correction:
- Color Correction — Fix technical issues, make it look natural
- Color Grading — Creative process, set the mood and style

Popular Color Grades:
- Cinematic — Teal shadows, orange skin tones
- Vintage — Faded, warm, desaturated
- Black and White — Remove all color
- Cool/Blue — Cold, sad, thriller look
- Warm/Golden — Happy, nostalgic, summer look""",
                    "code": ""
                }
            ]
        }
    ],

    "Data Science": [
        {
            "title": "Introduction to Data Science", "order": 1,
            "lessons": [
                {
                    "title": "What is Data Science?", "order": 1,
                    "content": """Data Science is an interdisciplinary field that uses scientific methods, algorithms, and systems to extract knowledge and insights from data.

Data Science combines:
- Statistics and Mathematics
- Programming (Python/R)
- Domain Knowledge
- Machine Learning
- Data Visualization

Data Science Workflow:
1. Problem Definition — What question are we answering?
2. Data Collection — Gather relevant data
3. Data Cleaning — Handle missing values, outliers
4. Exploratory Data Analysis — Understand the data
5. Modeling — Build predictive models
6. Evaluation — Test model performance
7. Deployment — Put model into production
8. Communication — Present findings

Career Paths:
- Data Analyst
- Data Scientist
- Machine Learning Engineer
- Business Intelligence Analyst
- Data Engineer""",
                    "code": """# Install required libraries
# pip install pandas numpy matplotlib seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Data Science libraries loaded successfully!")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")"""
                },
                {
                    "title": "NumPy Fundamentals", "order": 2,
                    "content": """NumPy (Numerical Python) is the foundation of data science in Python.

Why NumPy?
- Fast mathematical operations on arrays
- Much faster than regular Python lists
- Foundation for Pandas, Scikit-learn, TensorFlow

Key NumPy Concepts:
1. ndarray — N-dimensional array (core data structure)
2. Broadcasting — Operations on arrays of different shapes
3. Vectorization — Apply operations to entire arrays at once
4. Universal Functions (ufuncs) — Fast element-wise operations

Array vs List:
- NumPy arrays are faster and use less memory
- Arrays must contain same data type
- Arrays support mathematical operations directly""",
                    "code": """import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)
print("Shape:", arr2.shape)     # (2, 3)
print("Size:", arr2.size)       # 6

# Mathematical operations
print(arr1 * 2)                 # [2 4 6 8 10]
print(arr1 + 10)                # [11 12 13 14 15]
print(np.mean(arr1))            # 3.0
print(np.sum(arr1))             # 15
print(np.max(arr1))             # 5
print(np.min(arr1))             # 1

# Create special arrays
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
random = np.random.rand(3, 3)"""
                }
            ]
        },
        {
            "title": "Pandas for Data Analysis", "order": 2,
            "lessons": [
                {
                    "title": "DataFrames and Series", "order": 1,
                    "content": """Pandas is the most popular data manipulation library in Python.

Key Data Structures:
1. Series — 1D labeled array (like a column in Excel)
2. DataFrame — 2D labeled table (like an Excel spreadsheet)

Common Pandas Operations:
- Loading data (CSV, Excel, JSON, SQL)
- Viewing data (head, tail, info, describe)
- Selecting data (columns, rows, conditions)
- Cleaning data (handling missing values)
- Grouping and aggregating
- Merging and joining datasets
- Sorting and filtering""",
                    "code": """import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "Score": [85, 92, 78, 95],
    "City": ["Mumbai", "Delhi", "Pune", "Chennai"]
}
df = pd.DataFrame(data)
print(df)

# Basic operations
print(df.shape)          # (4, 4)
print(df.dtypes)         # data types
print(df.describe())     # statistics

# Select columns
print(df["Name"])
print(df[["Name", "Score"]])

# Filter rows
print(df[df["Age"] > 27])
print(df[df["Score"] >= 90])

# Sort
print(df.sort_values("Score", ascending=False))"""
                }
            ]
        },
        {
            "title": "Data Visualization", "order": 3,
            "lessons": [
                {
                    "title": "Matplotlib and Seaborn", "order": 1,
                    "content": """Data visualization helps you understand patterns and communicate insights.

Matplotlib — Basic plotting library:
- Line plots — Show trends over time
- Bar charts — Compare categories
- Scatter plots — Show relationships
- Histograms — Show distribution
- Pie charts — Show proportions

Seaborn — Statistical visualization:
- Built on top of Matplotlib
- More attractive default styles
- Better for statistical plots
- Heatmaps, box plots, violin plots

When to use which chart:
- Comparison → Bar chart
- Trend over time → Line chart
- Relationship → Scatter plot
- Distribution → Histogram or Box plot
- Proportion → Pie chart or Stacked bar""",
                    "code": """import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

# Bar chart
categories = ["Python", "JavaScript", "Java", "C++"]
values = [45, 30, 15, 10]
plt.bar(categories, values, color=["blue","orange","green","red"])
plt.title("Programming Language Popularity")
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color="purple", alpha=0.6)
plt.title("Scatter Plot")
plt.show()"""
                }
            ]
        }
    ],

    "Machine Learning": [
        {
            "title": "Introduction to Machine Learning", "order": 1,
            "lessons": [
                {
                    "title": "What is Machine Learning?", "order": 1,
                    "content": """Machine Learning (ML) is a subset of Artificial Intelligence that enables computers to learn from data without being explicitly programmed.

Types of Machine Learning:
1. Supervised Learning — Learns from labeled data
   - Classification (predict category)
   - Regression (predict number)
   
2. Unsupervised Learning — Finds patterns in unlabeled data
   - Clustering (group similar items)
   - Dimensionality Reduction
   
3. Reinforcement Learning — Learns by trial and error
   - Agent takes actions to maximize reward

ML Workflow:
1. Collect and prepare data
2. Choose a model
3. Train the model
4. Evaluate performance
5. Tune and improve
6. Deploy to production

Real-world Applications:
- Email spam detection
- Netflix recommendations
- Face recognition
- Self-driving cars
- Medical diagnosis""",
                    "code": """# Install scikit-learn
# pip install scikit-learn

from sklearn import datasets
import pandas as pd

# Load famous Iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

print(df.head())
print(f"Dataset shape: {df.shape}")
print(f"Classes: {iris.target_names}")"""
                }
            ]
        },
        {
            "title": "Supervised Learning", "order": 2,
            "lessons": [
                {
                    "title": "Linear Regression", "order": 1,
                    "content": """Linear Regression predicts a continuous numerical value based on input features.

Key Concepts:
- Dependent variable (y) — what we predict
- Independent variables (X) — features used for prediction
- Coefficient — how much y changes per unit X
- Intercept — value of y when X is 0
- Loss Function — measures prediction error (MSE)

Evaluation Metrics:
- MAE (Mean Absolute Error) — average absolute difference
- MSE (Mean Squared Error) — average squared difference
- RMSE (Root Mean Squared Error) — square root of MSE
- R² Score — how well model explains variance (0 to 1)

When to use Linear Regression:
- Predicting house prices
- Sales forecasting
- Stock price prediction
- Temperature prediction""",
                    "code": """from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2.5 * X + np.random.randn(100, 1) * 2

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print(f"R² Score: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.3f}")"""
                },
                {
                    "title": "Classification with Decision Trees", "order": 2,
                    "content": """Classification predicts which category an item belongs to.

Decision Tree:
- Tree-like model of decisions
- Each node is a feature
- Each branch is a decision rule
- Each leaf is an outcome

Advantages:
- Easy to understand and visualize
- Works with both numerical and categorical data
- No need to scale features
- Handles missing values

Disadvantages:
- Can overfit on training data
- Unstable (small changes cause big differences)
- Biased with imbalanced datasets

Evaluation Metrics for Classification:
- Accuracy — correct predictions / total predictions
- Precision — true positives / (true positives + false positives)
- Recall — true positives / (true positives + false negatives)
- F1 Score — harmonic mean of precision and recall""",
                    "code": """from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Decision Tree
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(classification_report(y_test, y_pred,
      target_names=iris.target_names))"""
                }
            ]
        }
    ],

    "Cyber Security": [
        {
            "title": "Introduction to Cyber Security", "order": 1,
            "lessons": [
                {
                    "title": "What is Cyber Security?", "order": 1,
                    "content": """Cyber Security is the practice of protecting computers, networks, programs, and data from digital attacks, damage, or unauthorized access.

Why Cyber Security Matters:
- Data breaches cost companies millions of dollars
- Personal information theft is increasing
- Critical infrastructure depends on digital systems
- Remote work has expanded attack surfaces

Types of Cyber Threats:
1. Malware — Malicious software (viruses, worms, ransomware)
2. Phishing — Fraudulent emails to steal credentials
3. Man-in-the-Middle — Intercepting communications
4. SQL Injection — Attacking databases via input fields
5. DDoS — Overwhelming servers with traffic
6. Social Engineering — Manipulating people psychologically

CIA Triad (Core Principles):
- Confidentiality — Only authorized access to data
- Integrity — Data is accurate and not tampered with
- Availability — Systems are accessible when needed

Career Paths:
- Ethical Hacker / Penetration Tester
- Security Analyst
- Incident Responder
- Security Engineer
- Chief Information Security Officer (CISO)""",
                    "code": ""
                },
                {
                    "title": "Types of Attacks", "order": 2,
                    "content": """Understanding attack types is essential for defense.

Common Attack Categories:

1. Network Attacks:
   - Packet Sniffing — Capturing network traffic
   - Port Scanning — Finding open ports and services
   - ARP Poisoning — Redirecting network traffic

2. Web Application Attacks:
   - SQL Injection — Manipulating database queries
   - XSS (Cross-Site Scripting) — Injecting malicious scripts
   - CSRF (Cross-Site Request Forgery) — Unauthorized actions
   - Directory Traversal — Accessing restricted files

3. Password Attacks:
   - Brute Force — Try all possible combinations
   - Dictionary Attack — Use common passwords list
   - Rainbow Tables — Pre-computed hash lookups
   - Credential Stuffing — Use leaked credentials

4. Social Engineering:
   - Phishing — Fake emails
   - Vishing — Fake phone calls
   - Pretexting — Creating false scenarios
   - Baiting — Leaving infected USB drives""",
                    "code": """# Example: Checking password strength (educational)
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%^&*)")
    
    strength = ["Very Weak","Weak","Fair","Strong","Very Strong"][score-1]
    return strength, feedback

strength, tips = check_password_strength("Hello@123")
print(f"Password Strength: {strength}")
for tip in tips:
    print(f"Tip: {tip}")"""
                }
            ]
        },
        {
            "title": "Network Security", "order": 2,
            "lessons": [
                {
                    "title": "Firewalls and VPNs", "order": 1,
                    "content": """Network security protects the integrity of your network and data.

Firewall:
A firewall monitors and controls incoming and outgoing network traffic based on security rules.

Types of Firewalls:
1. Packet Filtering — Checks packet headers
2. Stateful Inspection — Tracks connection state
3. Application Layer — Inspects content deeply
4. Next-Gen Firewall (NGFW) — Combines all types

VPN (Virtual Private Network):
Encrypts your internet connection and hides your IP address.

How VPN Works:
1. Your device connects to VPN server
2. Traffic is encrypted before leaving your device
3. VPN server sends traffic to the internet
4. Response comes back through VPN server to you

VPN Use Cases:
- Secure public Wi-Fi usage
- Bypass geographic restrictions
- Remote work security
- Privacy protection""",
                    "code": ""
                }
            ]
        }
    ],

    "Cloud Computing": [
        {
            "title": "Introduction to Cloud Computing", "order": 1,
            "lessons": [
                {
                    "title": "What is Cloud Computing?", "order": 1,
                    "content": """Cloud Computing is the delivery of computing services — including servers, storage, databases, networking, software, and intelligence — over the internet (the cloud).

Benefits of Cloud Computing:
- Cost Savings — Pay only for what you use
- Scalability — Scale up or down instantly
- Reliability — 99.9% uptime guarantees
- Speed — Deploy resources in minutes
- Global Reach — Servers worldwide
- Security — Enterprise-grade security

Cloud Service Models:
1. IaaS (Infrastructure as a Service)
   - Rent virtual machines, storage, networks
   - Example: AWS EC2, Azure Virtual Machines
   
2. PaaS (Platform as a Service)
   - Platform to build and deploy applications
   - Example: Google App Engine, Heroku
   
3. SaaS (Software as a Service)
   - Use software over the internet
   - Example: Gmail, Dropbox, Salesforce

Cloud Deployment Models:
- Public Cloud — Shared infrastructure (AWS, Azure, GCP)
- Private Cloud — Dedicated to one organization
- Hybrid Cloud — Mix of public and private
- Multi-Cloud — Using multiple cloud providers""",
                    "code": ""
                },
                {
                    "title": "AWS, Azure and Google Cloud", "order": 2,
                    "content": """The three major cloud providers dominate the market.

Amazon Web Services (AWS) — Market Leader:
- Launched in 2006, largest cloud provider
- 200+ services available
- Key services: EC2, S3, Lambda, RDS, CloudFront
- Strengths: Most services, largest community

Microsoft Azure — Enterprise Focus:
- Launched in 2010
- Strong integration with Microsoft products
- Key services: Azure VMs, Blob Storage, Azure Functions
- Strengths: Hybrid cloud, enterprise, Office 365 integration

Google Cloud Platform (GCP) — AI/ML Focus:
- Launched in 2011
- Strong in AI, ML, and data analytics
- Key services: Compute Engine, Cloud Storage, BigQuery
- Strengths: Data analytics, Kubernetes, AI/ML

Choosing a Cloud Provider:
- Existing Microsoft infrastructure → Azure
- AI/ML workloads → GCP
- General purpose / most options → AWS
- Cost optimization → Compare all three""",
                    "code": ""
                }
            ]
        },
        {
            "title": "Cloud Storage and Databases", "order": 2,
            "lessons": [
                {
                    "title": "Types of Cloud Storage", "order": 1,
                    "content": """Cloud storage allows you to store data on remote servers.

Types of Cloud Storage:

1. Object Storage:
   - Store any type of file as objects
   - Best for images, videos, backups
   - Examples: AWS S3, Google Cloud Storage, Azure Blob

2. Block Storage:
   - High-performance storage for VMs
   - Like a hard drive in the cloud
   - Examples: AWS EBS, Azure Disk Storage

3. File Storage:
   - Shared file system (like network drive)
   - Multiple servers can access simultaneously
   - Examples: AWS EFS, Azure Files

4. Database Storage:
   - Structured data in databases
   - SQL: RDS, Azure SQL, Cloud SQL
   - NoSQL: DynamoDB, Cosmos DB, Firestore

Storage Best Practices:
- Always backup critical data
- Use encryption for sensitive data
- Set proper access permissions
- Monitor storage costs
- Use lifecycle policies to archive old data""",
                    "code": ""
                }
            ]
        }
    ],

    "App Development": [
        {
            "title": "Introduction to App Development", "order": 1,
            "lessons": [
                {
                    "title": "Mobile App Development Overview", "order": 1,
                    "content": """Mobile app development is the process of creating software applications that run on mobile devices.

Types of Mobile Apps:
1. Native Apps:
   - Built specifically for one platform
   - iOS: Swift or Objective-C (Xcode)
   - Android: Kotlin or Java (Android Studio)
   - Best performance, full device access
   
2. Cross-Platform Apps:
   - One codebase for both iOS and Android
   - Flutter (Dart) — by Google
   - React Native (JavaScript) — by Meta
   - Faster development, cost-effective

3. Hybrid Apps:
   - Web app wrapped in native container
   - Ionic, Cordova
   - Less performance than native

Flutter vs React Native:
- Flutter — Better performance, beautiful UI, growing fast
- React Native — Larger community, uses JavaScript
- Both are excellent choices for cross-platform development

App Store Statistics:
- Google Play Store: 3.5+ million apps
- Apple App Store: 2.2+ million apps
- Average person uses 10 apps daily""",
                    "code": ""
                },
                {
                    "title": "Getting Started with Flutter", "order": 2,
                    "content": """Flutter is Google's UI toolkit for building natively compiled applications from a single codebase.

Why Flutter?
- Single codebase for iOS, Android, Web, Desktop
- Hot reload — see changes instantly
- Beautiful Material Design and Cupertino widgets
- Excellent performance (compiled to native code)
- Growing rapidly — used by Google, BMW, eBay

Flutter Setup:
1. Download Flutter SDK from flutter.dev
2. Extract and add to PATH
3. Install Android Studio
4. Run: flutter doctor (check setup)
5. Create project: flutter create my_app
6. Run: flutter run

Dart Language Basics:
- Flutter uses Dart programming language
- Similar to JavaScript and Java
- Strongly typed but with type inference
- Object-oriented with functional features

Flutter Widget Tree:
- Everything in Flutter is a widget
- Widgets are immutable UI components
- StatelessWidget — never changes
- StatefulWidget — can update dynamically""",
                    "code": """// Basic Flutter App Structure
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My First App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Hello Flutter!'),
      ),
      body: Center(
        child: Text(
          'Welcome to Flutter!',
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}"""
                }
            ]
        }
    ],

    "Database Management": [
        {
            "title": "Introduction to Databases", "order": 1,
            "lessons": [
                {
                    "title": "What is a Database?", "order": 1,
                    "content": """A database is an organized collection of structured information or data stored electronically.

Why Databases?
- Store large amounts of data efficiently
- Retrieve specific data quickly
- Multiple users can access simultaneously
- Data integrity and consistency
- Security and access control
- Backup and recovery

Types of Databases:
1. Relational (SQL) Databases:
   - Data stored in tables (rows and columns)
   - Uses SQL (Structured Query Language)
   - Examples: MySQL, PostgreSQL, SQLite, SQL Server
   - Best for: Structured data, complex queries

2. NoSQL Databases:
   - Flexible schema, various data models
   - Document: MongoDB, CouchDB
   - Key-Value: Redis, DynamoDB
   - Column: Cassandra, HBase
   - Graph: Neo4j
   - Best for: Unstructured data, scalability

Key Database Concepts:
- Table — Collection of related data
- Row (Record) — Single data entry
- Column (Field) — Attribute of data
- Primary Key — Unique identifier for each row
- Foreign Key — Link between two tables
- Index — Speeds up data retrieval""",
                    "code": ""
                },
                {
                    "title": "SQL Basics", "order": 2,
                    "content": """SQL (Structured Query Language) is used to communicate with relational databases.

SQL Categories:
1. DDL (Data Definition Language):
   - CREATE — Create tables/databases
   - ALTER — Modify structure
   - DROP — Delete tables/databases

2. DML (Data Manipulation Language):
   - SELECT — Read data
   - INSERT — Add new data
   - UPDATE — Modify existing data
   - DELETE — Remove data

3. DCL (Data Control Language):
   - GRANT — Give permissions
   - REVOKE — Remove permissions

SQL Constraints:
- NOT NULL — Column cannot be empty
- UNIQUE — All values must be different
- PRIMARY KEY — Unique identifier (NOT NULL + UNIQUE)
- FOREIGN KEY — Reference to another table
- CHECK — Value must meet a condition
- DEFAULT — Default value if none provided""",
                    "code": """-- Create a database
CREATE DATABASE school_db;
USE school_db;

-- Create a table
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    course VARCHAR(50),
    enrollment_date DATE DEFAULT CURRENT_DATE
);

-- Insert data
INSERT INTO students (name, email, age, course)
VALUES ('Alice Johnson', 'alice@email.com', 20, 'Python');

INSERT INTO students (name, email, age, course)
VALUES ('Bob Smith', 'bob@email.com', 22, 'Data Science');

-- Select data
SELECT * FROM students;
SELECT name, course FROM students WHERE age > 20;
SELECT * FROM students ORDER BY name ASC;

-- Update data
UPDATE students SET course = 'Machine Learning' WHERE name = 'Bob Smith';

-- Delete data
DELETE FROM students WHERE id = 1;"""
                }
            ]
        },
        {
            "title": "Advanced SQL", "order": 2,
            "lessons": [
                {
                    "title": "Joins and Relationships", "order": 1,
                    "content": """Joins combine rows from two or more tables based on a related column.

Types of JOINs:
1. INNER JOIN — Returns matching rows from both tables
2. LEFT JOIN — All rows from left + matching from right
3. RIGHT JOIN — All rows from right + matching from left
4. FULL OUTER JOIN — All rows from both tables

Database Relationships:
1. One-to-One (1:1)
   - One student has one profile
   
2. One-to-Many (1:N)
   - One course has many students
   
3. Many-to-Many (M:N)
   - Students can enroll in many courses
   - Courses can have many students
   - Requires a junction/bridge table

Normalization:
Process of organizing data to reduce redundancy.
- 1NF — Each column has atomic values
- 2NF — No partial dependencies
- 3NF — No transitive dependencies""",
                    "code": """-- Create related tables
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    instructor VARCHAR(100),
    price DECIMAL(8,2)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- INNER JOIN
SELECT s.name, c.course_name, e.enrollment_date
FROM students s
INNER JOIN enrollments e ON s.id = e.student_id
INNER JOIN courses c ON e.course_id = c.course_id;

-- LEFT JOIN (show all students, even not enrolled)
SELECT s.name, c.course_name
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
LEFT JOIN courses c ON e.course_id = c.course_id;

-- Aggregate functions
SELECT c.course_name, COUNT(e.student_id) as total_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
HAVING total_students > 5
ORDER BY total_students DESC;"""
                }
            ]
        }
    ],

    "Artificial Intelligence": [
        {
            "title": "Introduction to AI", "order": 1,
            "lessons": [
                {
                    "title": "What is Artificial Intelligence?", "order": 1,
                    "content": """Artificial Intelligence (AI) is the simulation of human intelligence in machines programmed to think and learn.

History of AI:
- 1950 — Alan Turing proposes the Turing Test
- 1956 — Term "Artificial Intelligence" coined at Dartmouth Conference
- 1997 — IBM Deep Blue defeats chess world champion
- 2011 — IBM Watson wins Jeopardy
- 2012 — Deep learning revolution begins (ImageNet)
- 2016 — AlphaGo defeats Go world champion
- 2022 — ChatGPT launched, AI goes mainstream
- 2023 — GPT-4, Gemini, Claude — AI assistants everywhere

AI Subfields:
1. Machine Learning — Learn from data
2. Deep Learning — Neural networks
3. Natural Language Processing (NLP) — Understand text/speech
4. Computer Vision — Understand images/video
5. Robotics — Physical AI systems
6. Expert Systems — Rule-based AI

AI Applications Today:
- Virtual assistants (Siri, Alexa, Google)
- Recommendation systems (Netflix, YouTube)
- Autonomous vehicles
- Medical diagnosis
- Fraud detection
- Language translation
- Image generation (DALL-E, Midjourney)""",
                    "code": """# Simple AI example — Rule-based chatbot
def simple_chatbot(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What can I do for you?",
        "how are you": "I'm doing great, thanks for asking!",
        "what is ai": "AI is the simulation of human intelligence in machines.",
        "bye": "Goodbye! Have a great day!",
    }
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I don't understand that yet. I'm still learning!"

# Test the chatbot
print(simple_chatbot("Hello!"))
print(simple_chatbot("What is AI?"))
print(simple_chatbot("How are you?"))"""
                },
                {
                    "title": "Neural Networks Basics", "order": 2,
                    "content": """Neural Networks are the foundation of modern AI.

Inspired by the Human Brain:
- Neurons — Basic processing units
- Synapses — Connections between neurons
- Artificial Neural Network mimics this structure

Structure of a Neural Network:
1. Input Layer — Receives raw data
2. Hidden Layers — Process and transform data
3. Output Layer — Produces the final result

Key Concepts:
- Weights — Strength of connections (learned during training)
- Bias — Offset value for each neuron
- Activation Function — Introduces non-linearity
   - ReLU — max(0, x) — most common
   - Sigmoid — outputs 0 to 1 (binary classification)
   - Softmax — outputs probabilities (multi-class)
   
Training Process:
1. Forward Pass — Input goes through network
2. Calculate Loss — Measure how wrong predictions are
3. Backpropagation — Calculate gradients
4. Update Weights — Gradient descent optimization
5. Repeat for many epochs""",
                    "code": """import numpy as np

# Simple Neural Network from scratch
class NeuralNetwork:
    def __init__(self):
        # Initialize random weights
        self.weights = np.random.randn(2, 1)
        self.bias = np.random.randn(1)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def forward(self, X):
        return self.sigmoid(np.dot(X, self.weights) + self.bias)
    
    def train(self, X, y, epochs=1000, lr=0.1):
        for _ in range(epochs):
            output = self.forward(X)
            error = y - output
            # Gradient descent
            self.weights += lr * np.dot(X.T, error * output * (1 - output))
            self.bias += lr * np.sum(error * output * (1 - output))

# XOR problem
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

nn = NeuralNetwork()
nn.train(X, y, epochs=10000)
print("Predictions:", nn.forward(X).round())"""
                }
            ]
        }
    ],

    "C++ Programming": [
        {
            "title": "Introduction to C++", "order": 1,
            "lessons": [
                {
                    "title": "What is C++?", "order": 1,
                    "content": """C++ is a powerful, high-performance, general-purpose programming language.

History:
- Created by Bjarne Stroustrup at Bell Labs in 1979
- Originally called "C with Classes"
- Renamed C++ in 1983 (++ means increment in C)
- C++11, C++14, C++17, C++20 — modern standards

Why Learn C++?
- Extremely fast execution speed
- Direct memory management control
- Foundation for systems programming
- Used in game engines, operating systems
- Helps understand how computers work at low level

C++ Applications:
- Game Development (Unreal Engine, Unity's core)
- Operating Systems (Windows, Linux kernel parts)
- Browsers (Chrome's V8 engine)
- Database engines (MySQL)
- Embedded systems and IoT
- High-frequency trading
- Computer graphics and VFX

C vs C++ vs Java vs Python:
- C++ — Fastest, manual memory, complex
- Java — Medium speed, automatic memory, OOP
- Python — Slowest, simplest, rapid development
- C — Fastest, lowest level, no OOP""",
                    "code": """// Your first C++ program
#include <iostream>
using namespace std;

int main() {
    // Print to console
    cout << "Hello, World!" << endl;
    
    // Variables
    string name = "Alice";
    int age = 20;
    
    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    
    // User input
    cout << "Enter your name: ";
    cin >> name;
    cout << "Hello, " << name << "!" << endl;
    
    return 0;
}"""
                },
                {
                    "title": "Variables and Data Types in C++", "order": 2,
                    "content": """C++ is a statically typed language — you must declare variable types.

Basic Data Types:
- int — Integer: -2,147,483,648 to 2,147,483,647
- long long — Large integer: up to 9.2 * 10^18
- float — Decimal (7 digits precision)
- double — Decimal (15 digits precision)
- char — Single character ('A', 'z', '5')
- bool — true or false
- string — Text (requires #include <string>)
- void — No value (used with functions)

Type Modifiers:
- signed — Can hold positive and negative
- unsigned — Only positive (doubles positive range)
- short — Smaller range, less memory
- long — Larger range, more memory

Constants:
- const int MAX = 100;  — cannot be changed
- #define PI 3.14159    — preprocessor constant

Type Casting:
- Implicit — automatic conversion
- Explicit — manual conversion using (type)""",
                    "code": """#include <iostream>
#include <string>
using namespace std;

int main() {
    // Basic data types
    int age = 25;
    float height = 5.11f;
    double salary = 75000.50;
    char grade = 'A';
    bool is_employed = true;
    string name = "John Doe";
    
    // Print all
    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "Height: " << height << endl;
    cout << "Salary: " << salary << endl;
    cout << "Grade: " << grade << endl;
    cout << "Employed: " << is_employed << endl;
    
    // Type casting
    int x = 10, y = 3;
    cout << "Integer division: " << x/y << endl;        // 3
    cout << "Float division: " << (float)x/y << endl;  // 3.333
    
    // Constants
    const double PI = 3.14159265;
    double area = PI * 5 * 5;
    cout << "Circle area: " << area << endl;
    
    return 0;
}"""
                }
            ]
        },
        {
            "title": "Object-Oriented Programming", "order": 2,
            "lessons": [
                {
                    "title": "Classes and Objects", "order": 1,
                    "content": """C++ is an object-oriented programming language.

OOP Concepts:
1. Class — Blueprint for creating objects
2. Object — Instance of a class
3. Encapsulation — Bundle data and methods together
4. Inheritance — Derive new class from existing class
5. Polymorphism — Same interface, different behavior
6. Abstraction — Hide implementation details

Class Structure:
- Access Specifiers:
  - public — Accessible from anywhere
  - private — Only accessible within class
  - protected — Accessible within class and derived classes

- Member Variables — Data stored in the class
- Member Functions (Methods) — Actions the class can perform
- Constructor — Special function called when object is created
- Destructor — Called when object is destroyed

Benefits of OOP:
- Code reusability through inheritance
- Data hiding through encapsulation
- Easy to maintain and modify
- Models real-world entities naturally""",
                    "code": """#include <iostream>
#include <string>
using namespace std;

// Define a class
class Student {
private:
    string name;
    int age;
    float gpa;

public:
    // Constructor
    Student(string n, int a, float g) {
        name = n;
        age = a;
        gpa = g;
    }
    
    // Getter methods
    string getName() { return name; }
    int getAge() { return age; }
    float getGPA() { return gpa; }
    
    // Method
    void display() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "GPA: " << gpa << endl;
    }
    
    string getGrade() {
        if (gpa >= 3.7) return "A";
        else if (gpa >= 3.3) return "B+";
        else if (gpa >= 3.0) return "B";
        else return "C";
    }
};

int main() {
    // Create objects
    Student s1("Alice", 20, 3.8);
    Student s2("Bob", 22, 3.2);
    
    s1.display();
    cout << "Grade: " << s1.getGrade() << endl;
    
    s2.display();
    cout << "Grade: " << s2.getGrade() << endl;
    
    return 0;
}"""
                }
            ]
        }
    ]
}


class Command(BaseCommand):
    help = 'Add chapters and lessons to all courses'

    def handle(self, *args, **kwargs):
        for course_name, chapters in COURSE_CONTENT.items():
            try:
                course = Course.objects.get(course_name=course_name)
            except Course.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Course not found: {course_name}'))
                continue

            # Delete existing chapters
            course.chapters.all().delete()

            for ch_data in chapters:
                chapter = Chapter.objects.create(
                    course=course,
                    title=ch_data['title'],
                    order=ch_data['order']
                )
                for les_data in ch_data['lessons']:
                    Lesson.objects.create(
                        chapter=chapter,
                        title=les_data['title'],
                        content=les_data['content'],
                        code_example=les_data.get('code', ''),
                        order=les_data['order']
                    )
                self.stdout.write(f"  Chapter: {ch_data['title']} ({len(ch_data['lessons'])} lessons)")

            self.stdout.write(self.style.SUCCESS(f"Done: {course_name}"))

        self.stdout.write(self.style.SUCCESS('\nAll courses content added successfully!'))