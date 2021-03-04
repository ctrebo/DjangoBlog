from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import BlogAuthor, BlogComment, Blog

class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()
        
        blog_author = BlogAuthor.objects.create(user=test_user1, bio="My bio")
        blog = Blog.objects.create(name="test blog", author=blog_author, description="The description is the desctiption")
        
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('blogs'))
        self.assertRedirects(response, '/accounts/login/?next=/blog/blogs/')
    
    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get("/blog/blogs/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('blogs'))

        # Check that we got a response "success"
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "blog/blog_list.html")

class BlogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()
        
        blog_author = BlogAuthor.objects.create(user=test_user1, bio="My bio")
        blog = Blog.objects.create(name="test blog", author=blog_author, description="The description is the desctiption")
        
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('blog-detail', kwargs={'pk':1}))
        self.assertRedirects(response, '/accounts/login/?next=/blog/blogs/1')
    
    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        blog = Blog.objects.get(id=1)
        response = self.client.get(blog.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        # blog = Blog.objects.get(id=1)
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('blog-detail', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('blog-detail', kwargs={'pk':1}))

        # Check that we got a response "success"
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "blog/blog_detail.html")

class BlogAuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()
        
        blog_author = BlogAuthor.objects.create(user=test_user1, bio="My bio")
        
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('bloggers'))
        self.assertRedirects(response, '/accounts/login/?next=/blog/bloggers/')
    
    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get("/blog/bloggers/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('bloggers'))

        # Check that we got a response "success"
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "blog/blogauthor_list.html")

class BlogListbyAuthorViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()
        
        blog_author = BlogAuthor.objects.create(user=test_user1, bio="My bio")
        blog_author.save()
        blog = Blog.objects.create(name="test blog", author=blog_author, description="The description is the desctiption")
        
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('blogger-detail',  kwargs={'pk':1}))
        self.assertRedirects(response, '/accounts/login/?next=/blog/bloggers/1')
    
    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        blog_author = BlogAuthor.objects.get(id=1)
        response = self.client.get(blog_author.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('blogger-detail', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('blogger-detail', kwargs={'pk':1}))

        # Check that we got a response "success"
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

        # self.assertEqual(str(response.context['blogger']), 'blog_author')


        self.assertTemplateUsed(response, "blog/blog_list_by_author.html")


