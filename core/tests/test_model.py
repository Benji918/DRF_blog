from django.test import TestCase
from core import models
from django.contrib.auth import get_user_model


def create_user(**params):
    """Helper function to create user objects"""
    defaults = {
        'username': 'johndoe',
        'email': 'test@example.com',
        'password': 'testpass123',
    }
    defaults.update(params)
    user = get_user_model().objects.create_user(**defaults)
    return user


def create_blog_post(**params):
    """Helper function to create blog objects"""
    defaults = {
        'title': 'dummy title',
        'content': 'Dummy content',
        'author': create_user(email='fdfd@gmail.com'),
    }
    defaults.update(params)
    blog_post = models.BlogPost.objects.create(**defaults)
    return blog_post


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_success(self):
        """Test creating a user successfully"""
        email = 'kodi@example.com'
        password = 'testpass12345'
        user = create_user(email=email, password=password)

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_blank_email(self):
        """Test creating a user with a blank email address"""
        with self.assertRaises(ValueError):
            create_user(email='', password='testpass123')

    def test_create_user_with_admin_false(self):
        """Test create user with admin set as false"""
        user = create_user()

        self.assertFalse(user.is_admin)

    def test_create_superuser(self):
        """Test creation of superuser"""
        email = 'test@example.com'
        password = '123456789'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_blog_success(self):
        """Test creating a blog successfully"""
        title = 'Dream team'
        content = 'dream content'
        user = create_user(email='benji@example.com')
        blog = create_blog_post(
            title=title,
            content=content,
            author=user
        )

        self.assertEquals(blog.author, user)
        self.assertEquals(blog.title, title)
        self.assertEquals(blog.content, content)

    def test_create_blog_without_title(self):
        """Test creating a blog with no title"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create(email='hihis@gmail.com', password='fj9jf9jf')
            blog = create_blog_post(
                title='',
                content='dream contssent',
                author=user
            )


