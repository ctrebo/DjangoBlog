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
        blog_author = BlogAuthor.objects.get(id=1)
        max_length = blog_author._meta.get_field('bio').max_length
        self.assertEqual(max_length, 400)    


    def test_object_name_is_user_name(self):
        blog_author = BlogAuthor.objects.get(id=1)
        expected_object_name = f'{blog_author.user.username}'
        self.assertEqual(expected_object_name, str(blog_author))

    def test_get_absolute_url(self):
        blog_author = BlogAuthor.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(blog_author.get_absolute_url(), '/blog/bloggers/1')


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user=User.objects.create_user('foo', password='bar')
        blog_author = BlogAuthor.objects.create(user=user, bio="My bio")
        blog = Blog.objects.create(name="test blog", author=blog_author, description="The description is the desctiption")

    
    def test_name_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")
    
    def test_author_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_bio_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_name_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('name').max_length
        self.assertEqual(max_length, 200) 

    def test_description_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEqual(max_length, 2000)

    def test_object_name_is_blog_name(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f'{blog.name}'
        self.assertEqual(expected_object_name, str(blog))

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(blog.get_absolute_url(), '/blog/blogs/1') 

class TestBlogComment(TestCase):
    @classmethod
    def setUpTestData(cls):
        user=User.objects.create_user('foo', password='bar')
        blog_author = BlogAuthor.objects.create(user=user, bio="My bio")
        blog = Blog.objects.create(name="test blog", author=blog_author, description="The description is the desctiption")
        blog_comment = BlogComment.objects.create(description="Blog description", author=user, blog=blog)

        
    
    def test_description_label(self):
        blog_comment = BlogComment.objects.get(id=1)
        field_label = blog_comment._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_author_label(self):
        blog_comment = BlogComment.objects.get(id=1)
        field_label = blog_comment._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_blog_label(self):
        blog_comment = BlogComment.objects.get(id=1)
        field_label = blog_comment._meta.get_field("blog").verbose_name
        self.assertEqual(field_label, "blog")

    def test_description_max_length(self):
        blog_comment = BlogComment.objects.get(id=1)
        max_length = blog_comment._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)


