from django.test import TestCase
from ..models import BlogAuthor, BlogComment, Blog
from django.contrib.auth.models import User

class BlogAuthorTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user=User.objects.create_user('foo', password='bar')
        BlogAuthor.objects.create(user=user, bio="My bio")

    def test_user_label(self):
        blog_author = BlogAuthor.objects.get(id=1)
        field_label = blog_author._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")
    
    def test_user_label(self):
        blog_author = BlogAuthor.objects.get(id=1)
        field_label = blog_author._meta.get_field("bio").verbose_name
        self.assertEqual(field_label, "bio")

    def test_user_label(self):
        blog_author = BlogAuthor.objects.get(id=1)
        field_label = blog_author._meta.get_field("prof_picture").verbose_name
        self.assertEqual(field_label, "prof picture")

    def test_bio_max_length(self):
        author = Author.objects.get(id=1)
        max_length = blog_author._meta.get_field('bio').max_length
        self.assertEqual(max_length, 400)    


    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')