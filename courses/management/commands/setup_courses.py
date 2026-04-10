import urllib.request
import os
from django.core.management.base import BaseCommand
from courses.models import Course

COURSES = [
    {
        "name": "Python Programming",
        "category": "programming",
        "price": 999,
        "description": "Learn Python from scratch. Covers variables, loops, functions, OOP, file handling and more. Perfect for beginners who want to start their coding journey.",
        "image": "https://images.unsplash.com/photo-1649180556628-9ba704115795?w=800&q=90",
        "filename": "python.jpg"
    },
    {
        "name": "Web Development",
        "category": "web",
        "price": 1499,
        "description": "Master HTML, CSS, JavaScript, and Django. Build real-world websites from scratch with modern design techniques and best practices.",
        "image": "https://images.unsplash.com/photo-1627398242454-45a1465c2479?w=800&q=90",
        "filename": "web.jpg"
    },
    {
        "name": "Data Science",
        "category": "datascience",
        "price": 1999,
        "description": "Explore data analysis, visualization, and machine learning using Python, Pandas, NumPy, and Matplotlib. Learn to derive insights from real datasets.",
        "image": "https://images.unsplash.com/photo-1666875753105-c63a6f3bdc86?w=800&q=90",
        "filename": "datascience.jpg"
    },
    {
        "name": "Machine Learning",
        "category": "ml",
        "price": 2499,
        "description": "Deep dive into ML algorithms, supervised and unsupervised learning, model evaluation, and deployment using Scikit-learn and TensorFlow.",
        "image": "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=800&q=90",
        "filename": "ml.jpg"
    },
    {
        "name": "Cyber Security",
        "category": "cyber",
        "price": 1799,
        "description": "Learn ethical hacking, network security, penetration testing, cryptography and how to protect systems from cyber threats.",
        "image": "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=800&q=90",
        "filename": "cyber.jpg"
    },
    {
        "name": "Cloud Computing",
        "category": "cloud",
        "price": 1599,
        "description": "Understand cloud architecture, AWS, Azure, and Google Cloud. Learn to deploy, manage and scale applications on the cloud.",
        "image": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=800&q=90",
        "filename": "cloud.jpg"
    },
    {
        "name": "App Development",
        "category": "app",
        "price": 1299,
        "description": "Build Android and iOS apps using Flutter and Dart. Create beautiful cross-platform mobile applications from scratch.",
        "image": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&q=90",
        "filename": "app.jpg"
    },
    {
        "name": "Database Management",
        "category": "database",
        "price": 0,
        "description": "Learn SQL, MySQL, PostgreSQL and database design principles. Understand queries, joins, indexing and database optimization techniques.",
        "image": "https://images.unsplash.com/photo-1489875347897-49f64b51c1f8?w=800&q=90",
        "filename": "database.jpg"
    },
    {
        "name": "Artificial Intelligence",
        "category": "ai",
        "price": 2999,
        "description": "Learn the foundations of AI including neural networks, deep learning, NLP, and computer vision using Python and TensorFlow.",
        "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&q=90",
        "filename": "ai.jpg"
    },
    {
        "name": "C++ Programming",
        "category": "programming",
        "price": 799,
        "description": "Master C++ programming language from basics to advanced. Learn OOP, STL, memory management, and build efficient applications.",
        "image": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=800&q=90",
        "filename": "cpp.jpg"
    },
]


class Command(BaseCommand):
    help = 'Setup all courses with images and prices'

    def handle(self, *args, **kwargs):
        media_path = 'media/courses/'
        os.makedirs(media_path, exist_ok=True)

        for c in COURSES:
            filepath = os.path.join(media_path, c['filename'])

            if not os.path.exists(filepath):
                self.stdout.write(f"Downloading image for {c['name']}...")
                try:
                    req = urllib.request.Request(
                        c['image'],
                        headers={'User-Agent': 'Mozilla/5.0'}
                    )
                    with urllib.request.urlopen(req) as response:
                        with open(filepath, 'wb') as f:
                            f.write(response.read())
                    self.stdout.write(self.style.SUCCESS(f"  Downloaded: {c['filename']}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"  Failed: {e}"))
                    continue

            course, created = Course.objects.update_or_create(
                course_name=c['name'],
                defaults={
                    'category': c['category'],
                    'price': c['price'],
                    'description': c['description'],
                    'image_url': f"courses/{c['filename']}",
                    'is_active': True,
                }
            )
            action = "Created" if created else "Updated"
            price_str = "Free" if c['price'] == 0 else f"Rs.{c['price']}"
            self.stdout.write(self.style.SUCCESS(
                f"  {action}: {c['name']} — {price_str}"
            ))

        self.stdout.write(self.style.SUCCESS('\nAll courses setup successfully!'))
