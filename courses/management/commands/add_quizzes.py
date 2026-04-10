from django.core.management.base import BaseCommand
from courses.models import Chapter, Quiz, Question


class Command(BaseCommand):
    help = 'Add quizzes to all chapters'

    def handle(self, *args, **kwargs):
        quizzes = [
            {
                'chapter': 'Introduction to Python',
                'title': 'Python Basics Quiz',
                'questions': [
                    ('What is Python?', 'A snake', 'A programming language', 'An operating system', 'A database', 'B'),
                    ('Which symbol is used for comments in Python?', '//', '#', '/*', '--', 'B'),
                    ('What function prints output in Python?', 'echo()', 'console.log()', 'print()', 'write()', 'C'),
                    ('Python is which type of language?', 'Compiled', 'Interpreted', 'Assembly', 'Machine', 'B'),
                    ('Which extension is used for Python files?', '.java', '.cpp', '.py', '.js', 'C'),
                ]
            },
            {
                'chapter': 'Variables and Data Types',
                'title': 'Variables & Data Types Quiz',
                'questions': [
                    ('Which is a valid variable name?', '2name', 'my-var', 'my_var', 'my var', 'C'),
                    ('What type is the value 3.14 in Python?', 'int', 'float', 'str', 'bool', 'B'),
                    ('How do you create a string in Python?', 'Using []', 'Using {}', 'Using quotes', 'Using ()', 'C'),
                    ('What does type() function return?', 'Value of variable', 'Data type of variable', 'Size of variable', 'Name of variable', 'B'),
                    ('Which is NOT a Python data type?', 'int', 'float', 'char', 'bool', 'C'),
                ]
            },
            {
                'chapter': 'Control Flow',
                'title': 'Control Flow Quiz',
                'questions': [
                    ('Which keyword starts a conditional block?', 'when', 'if', 'check', 'case', 'B'),
                    ('What does a for loop do?', 'Defines a function', 'Iterates over a sequence', 'Checks condition', 'Imports module', 'B'),
                    ('Which keyword skips to next iteration?', 'skip', 'break', 'continue', 'pass', 'C'),
                    ('What does break do in a loop?', 'Skips one iteration', 'Exits the loop', 'Pauses loop', 'Restarts loop', 'B'),
                    ('Correct syntax for if-else?', 'if x > 0 then:', 'if (x > 0):', 'if x > 0:', 'if x > 0 {', 'C'),
                ]
            },
            {
                'chapter': 'Functions',
                'title': 'Functions Quiz',
                'questions': [
                    ('How do you define a function in Python?', 'function myFunc():', 'def myFunc():', 'func myFunc():', 'define myFunc():', 'B'),
                    ('What keyword returns a value from function?', 'give', 'send', 'return', 'output', 'C'),
                    ('What is a parameter?', 'Function name', 'Variable inside loop', 'Input to a function', 'Output of function', 'C'),
                    ('What is recursion?', 'Loop inside loop', 'Function calling itself', 'Import statement', 'Class method', 'B'),
                    ('Default parameter value is set with?', ':', ':=', '=', '==', 'C'),
                ]
            },
            {
                'chapter': 'Introduction to Video Editing',
                'title': 'Video Editing Basics Quiz',
                'questions': [
                    ('Which software is popular for video editing?', 'MS Word', 'Adobe Premiere Pro', 'Notepad', 'Excel', 'B'),
                    ('FPS stands for?', 'File Per Second', 'Frames Per Second', 'Format Per Scene', 'Fast Processing Speed', 'B'),
                    ('A timeline in video editing is?', 'Clock on screen', 'Where clips are arranged', 'Export settings', 'Audio mixer', 'B'),
                    ('What is a cut in video editing?', 'Deleting a file', 'Instant transition between clips', 'Adding music', 'Color grading', 'B'),
                    ('Resolution 1920x1080 is called?', '4K', '720p', 'Full HD', '8K', 'C'),
                ]
            },
            {
                'chapter': 'Cutting and Trimming',
                'title': 'Cutting & Trimming Quiz',
                'questions': [
                    ('Trimming a clip means?', 'Adding effects', 'Shortening clip length', 'Changing color', 'Adding audio', 'B'),
                    ('J-cut is a type of?', 'Color effect', 'Audio transition where audio starts before video', 'Video filter', 'Export format', 'B'),
                    ('What is B-roll footage?', 'Main footage', 'Supplementary/cutaway footage', 'Deleted scenes', 'Audio track', 'B'),
                    ('Razor tool in editing is used for?', 'Adding text', 'Cutting clips', 'Color grading', 'Exporting', 'B'),
                    ('What is a jump cut?', 'Slow motion effect', 'Abrupt cut between similar shots', 'Fade transition', 'Audio cut', 'B'),
                ]
            },
            {
                'chapter': 'Color Grading',
                'title': 'Color Grading Quiz',
                'questions': [
                    ('Color grading is used to?', 'Add subtitles', 'Enhance visual mood and tone', 'Speed up video', 'Add transitions', 'B'),
                    ('LUT stands for?', 'Light Utility Tool', 'Look Up Table', 'Layer Under Tone', 'Luma Under Track', 'B'),
                    ('Color correction vs color grading?', 'Same thing', 'Correction fixes exposure, grading adds style', 'Grading fixes exposure', 'Neither changes color', 'B'),
                    ('Which tool adjusts brightness and contrast?', 'Razor', 'Lumetri Color', 'Pen tool', 'Text tool', 'B'),
                    ('Saturation controls?', 'Brightness', 'Color intensity', 'Sharpness', 'Frame rate', 'B'),
                ]
            },
            {
                'chapter': 'Introduction to Data Science & NumPy',
                'title': 'NumPy & Data Science Basics Quiz',
                'questions': [
                    ('What does NumPy stand for?', 'Numerical Python', 'New Python', 'Number Package', 'None of these', 'A'),
                    ('Which function creates a NumPy array?', 'np.create()', 'np.array()', 'np.list()', 'np.new()', 'B'),
                    ('What is a DataFrame?', '1D array', '2D table with labels', 'Dictionary', 'Function', 'B'),
                    ('Which library is best for data visualization?', 'NumPy', 'Pandas', 'Matplotlib', 'Scikit', 'C'),
                    ('Shape of NumPy array is accessed by?', '.size', '.shape', '.dim', '.length', 'B'),
                ]
            },
            {
                'chapter': 'Pandas for Data Analysis',
                'title': 'Pandas Quiz',
                'questions': [
                    ('How to read a CSV file in Pandas?', 'pd.open()', 'pd.read_csv()', 'pd.load()', 'pd.import()', 'B'),
                    ('Which method shows first 5 rows?', 'df.start()', 'df.top()', 'df.head()', 'df.first()', 'C'),
                    ('How to select a column in DataFrame?', "df['col']", 'df.get(col)', 'df->col', 'df::col', 'A'),
                    ('Which method drops null values?', 'df.remove()', 'df.dropna()', 'df.clean()', 'df.delete()', 'B'),
                    ('groupby() is used for?', 'Sorting data', 'Grouping and aggregating', 'Filtering rows', 'Merging tables', 'B'),
                ]
            },
            {
                'chapter': 'Data Visualization',
                'title': 'Data Visualization Quiz',
                'questions': [
                    ('Which library is used for plotting in Python?', 'NumPy', 'Pandas', 'Matplotlib', 'Requests', 'C'),
                    ('A bar chart is best for?', 'Time series', 'Comparing categories', 'Showing distribution', 'Correlation', 'B'),
                    ('Seaborn is built on top of?', 'Pandas', 'NumPy', 'Matplotlib', 'Scikit-learn', 'C'),
                    ('plt.show() is used to?', 'Save plot', 'Display the plot', 'Clear plot', 'Resize plot', 'B'),
                    ('Histogram shows?', 'Category comparison', 'Distribution of data', 'Trend over time', 'Correlation', 'B'),
                ]
            },
            {
                'chapter': 'Introduction to ML',
                'title': 'Machine Learning Basics Quiz',
                'questions': [
                    ('What is Machine Learning?', 'Programming robots', 'Systems learning from data', 'Hardware design', 'Network security', 'B'),
                    ('Which is supervised learning?', 'Clustering', 'Classification', 'Association', 'Dimensionality Reduction', 'B'),
                    ('Which library is used for ML in Python?', 'Django', 'Flask', 'Scikit-learn', 'NumPy', 'C'),
                    ('Training data is used to?', 'Test the model', 'Train/fit the model', 'Deploy the model', 'Visualize data', 'B'),
                    ('Overfitting means?', 'Model too simple', 'Model performs well on train but poor on test', 'Model not trained', 'Fast training', 'B'),
                ]
            },
            {
                'chapter': 'Supervised Learning',
                'title': 'Supervised Learning Quiz',
                'questions': [
                    ('Supervised learning requires?', 'Unlabeled data', 'Labeled data', 'No data', 'Random data', 'B'),
                    ('Linear regression is used for?', 'Classification', 'Clustering', 'Predicting continuous values', 'Dimensionality reduction', 'C'),
                    ('Decision tree splits data based on?', 'Random choice', 'Feature values', 'User input', 'Time', 'B'),
                    ('What is accuracy in classification?', 'Speed of model', 'Correct predictions / total predictions', 'Training time', 'Model size', 'B'),
                    ('SVM stands for?', 'Simple Vector Model', 'Support Vector Machine', 'System Variable Method', 'Supervised Value Model', 'B'),
                ]
            },
            {
                'chapter': 'Introduction to Cyber Security',
                'title': 'Cyber Security Basics Quiz',
                'questions': [
                    ('What is phishing?', 'A type of virus', 'Fraudulent attempt to steal info', 'Network protocol', 'Firewall type', 'B'),
                    ('What does VPN stand for?', 'Virtual Private Network', 'Very Private Node', 'Virtual Protocol Number', 'Verified Private Network', 'A'),
                    ('Which is strongest password?', 'password123', 'john1990', 'P@ssw0rd!#2024', 'qwerty', 'C'),
                    ('Malware is?', 'Useful software', 'Malicious software', 'A programming language', 'A browser', 'B'),
                    ('Two-factor authentication adds?', 'Speed', 'Extra security layer', 'New password', 'Encryption', 'B'),
                ]
            },
            {
                'chapter': 'Network Security',
                'title': 'Network Security Quiz',
                'questions': [
                    ('A firewall is used to?', 'Speed up internet', 'Monitor and control network traffic', 'Store passwords', 'Compress files', 'B'),
                    ('DoS attack stands for?', 'Domain of Service', 'Denial of Service', 'Data on Server', 'Disk on System', 'B'),
                    ('HTTPS is secure because of?', 'Faster speed', 'SSL/TLS encryption', 'Better browser', 'Bigger bandwidth', 'B'),
                    ('What is a DMZ in networking?', 'Dangerous Memory Zone', 'Demilitarized Zone - buffer between networks', 'Domain Management Zone', 'Data Migration Zone', 'B'),
                    ('Which port does HTTPS use?', '80', '21', '443', '22', 'C'),
                ]
            },
            {
                'chapter': 'Introduction to Cloud Computing',
                'title': 'Cloud Computing Basics Quiz',
                'questions': [
                    ('What is cloud computing?', 'Local storage', 'Delivering services over internet', 'Hardware maintenance', 'Programming language', 'B'),
                    ('IaaS stands for?', 'Internet as a Service', 'Infrastructure as a Service', 'Integration as a Service', 'Interface as a Service', 'B'),
                    ('Which is NOT a cloud provider?', 'AWS', 'Azure', 'Google Cloud', 'Django', 'D'),
                    ('Public cloud is?', 'Private to one org', 'Shared infrastructure open to all', 'Only on-premise', 'Hybrid model', 'B'),
                    ('S3 in AWS is used for?', 'Computing', 'Databases', 'Object Storage', 'Networking', 'C'),
                ]
            },
            {
                'chapter': 'Cloud Storage and Databases',
                'title': 'Cloud Storage Quiz',
                'questions': [
                    ('Object storage stores data as?', 'Tables', 'Files in folders', 'Objects with metadata', 'Rows and columns', 'C'),
                    ('AWS RDS is used for?', 'Object storage', 'Managed relational databases', 'Serverless functions', 'CDN', 'B'),
                    ('CDN stands for?', 'Central Data Node', 'Content Delivery Network', 'Cloud Data Network', 'Centralized Domain Name', 'B'),
                    ('Blob storage is offered by?', 'AWS', 'Google Cloud', 'Microsoft Azure', 'Heroku', 'C'),
                    ('Scalability in cloud means?', 'Fixed resources', 'Ability to increase/decrease resources', 'Only adding servers', 'Removing old data', 'B'),
                ]
            },
            {
                'chapter': 'Introduction to App Development & Flutter',
                'title': 'App Development & Flutter Quiz',
                'questions': [
                    ('Flutter is developed by?', 'Microsoft', 'Apple', 'Google', 'Facebook', 'C'),
                    ('Flutter uses which programming language?', 'Java', 'Kotlin', 'Dart', 'Swift', 'C'),
                    ('Flutter is used for?', 'Web only', 'Mobile only', 'Cross-platform apps', 'Server only', 'C'),
                    ('A Widget in Flutter is?', 'A database', 'UI building block', 'A function', 'A server', 'B'),
                    ('Hot reload in Flutter allows?', 'Restart server', 'See changes instantly without full restart', 'Build APK', 'Run tests', 'B'),
                ]
            },
            {
                'chapter': 'Introduction to Databases & SQL',
                'title': 'Database & SQL Basics Quiz',
                'questions': [
                    ('What does SQL stand for?', 'Structured Query Language', 'Simple Query Logic', 'System Query Layer', 'Stored Query List', 'A'),
                    ('Which command retrieves data?', 'INSERT', 'UPDATE', 'SELECT', 'DELETE', 'C'),
                    ('Primary key must be?', 'Null', 'Duplicate', 'Unique and not null', 'String only', 'C'),
                    ('Which command adds a new row?', 'ADD', 'INSERT INTO', 'UPDATE', 'CREATE', 'B'),
                    ('What is a foreign key?', 'Key from another table referencing primary key', 'Encrypted key', 'Primary key copy', 'Null key', 'A'),
                ]
            },
            {
                'chapter': 'Advanced SQL and Joins',
                'title': 'Advanced SQL & Joins Quiz',
                'questions': [
                    ('INNER JOIN returns?', 'All rows from both tables', 'Only matching rows from both tables', 'All rows from left table', 'All rows from right table', 'B'),
                    ('LEFT JOIN returns?', 'Only matching rows', 'All left table rows + matching right rows', 'All right table rows', 'No rows', 'B'),
                    ('GROUP BY is used with?', 'WHERE clause', 'Aggregate functions like COUNT, SUM', 'ORDER BY only', 'INSERT statement', 'B'),
                    ('HAVING clause filters?', 'Individual rows', 'Grouped results', 'Columns', 'Tables', 'B'),
                    ('What does COUNT(*) do?', 'Sums values', 'Counts all rows', 'Averages values', 'Finds max', 'B'),
                ]
            },
            {
                'chapter': 'Introduction to AI & Neural Networks',
                'title': 'AI & Neural Networks Quiz',
                'questions': [
                    ('What is Artificial Intelligence?', 'Robots only', 'Simulation of human intelligence by machines', 'Computer hardware', 'Internet protocol', 'B'),
                    ('A neural network is inspired by?', 'Computer chips', 'Human brain', 'Solar system', 'DNA structure', 'B'),
                    ('Deep learning uses?', 'Shallow networks', 'Single layer', 'Multiple hidden layers', 'No layers', 'C'),
                    ('Which is an AI application?', 'Spreadsheet', 'Calculator', 'Image recognition', 'Notepad', 'C'),
                    ('Activation function in neural network?', 'Starts training', 'Introduces non-linearity', 'Loads data', 'Saves model', 'B'),
                ]
            },
            {
                'chapter': 'Introduction to C++',
                'title': 'C++ Basics Quiz',
                'questions': [
                    ('C++ is developed by?', 'Dennis Ritchie', 'Bjarne Stroustrup', 'James Gosling', 'Guido van Rossum', 'B'),
                    ('Which header file is needed for cout?', '<stdio.h>', '<string>', '<iostream>', '<math.h>', 'C'),
                    ('How to print in C++?', 'print()', 'printf()', 'cout<<', 'System.out.print()', 'C'),
                    ('Which symbol ends a statement in C++?', ':', '.', ';', ',', 'C'),
                    ('C++ supports which programming paradigm?', 'Only procedural', 'Only OOP', 'Both procedural and OOP', 'Functional only', 'C'),
                ]
            },
            {
                'chapter': 'OOP and Classes in C++',
                'title': 'OOP & Classes Quiz',
                'questions': [
                    ('OOP stands for?', 'Object Oriented Programming', 'Open Oriented Process', 'Output Operation Program', 'Online Object Protocol', 'A'),
                    ('A class in C++ is?', 'A variable', 'Blueprint for objects', 'A loop', 'A function', 'B'),
                    ('Which is a pillar of OOP?', 'Compilation', 'Encapsulation', 'Execution', 'Declaration', 'B'),
                    ('Constructor is called?', 'Manually by user', 'Automatically when object is created', 'Only once in program', 'At program end', 'B'),
                    ('Inheritance allows?', 'Faster execution', 'Child class to use parent class properties', 'Multiple outputs', 'Automatic testing', 'B'),
                ]
            },
        ]

        created = 0
        skipped = 0

        for quiz_data in quizzes:
            chapter_title = quiz_data['chapter']
            try:
                chapter = Chapter.objects.get(title=chapter_title)
            except Chapter.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Chapter not found: {chapter_title}'))
                skipped += 1
                continue
            except Chapter.MultipleObjectsReturned:
                chapter = Chapter.objects.filter(title=chapter_title).first()

            quiz, was_created = Quiz.objects.get_or_create(
                chapter=chapter,
                defaults={'title': quiz_data['title'], 'pass_marks': 60}
            )

            if not was_created:
                self.stdout.write(self.style.WARNING(f'Quiz already exists: {quiz_data["title"]}'))
                skipped += 1
                continue

            for i, (qtext, oa, ob, oc, od, correct) in enumerate(quiz_data['questions']):
                Question.objects.create(
                    quiz=quiz,
                    question_text=qtext,
                    option_a=oa,
                    option_b=ob,
                    option_c=oc,
                    option_d=od,
                    correct_option=correct,
                    order=i
                )

            self.stdout.write(self.style.SUCCESS(f'Quiz created: {quiz_data["title"]}'))
            created += 1

        self.stdout.write(self.style.SUCCESS(f'\nDone! {created} quizzes created, {skipped} skipped.'))