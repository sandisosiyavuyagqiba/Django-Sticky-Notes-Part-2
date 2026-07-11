# posts/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Post, Author

class PostModelTest(TestCase):
    def setUp(self):
        # Create an Author object
        author = Author.objects.create(name='Test Author')
        # Create a Post object for testing
        Post.objects.create(title='Test Post', content='This is a test post.', author=author)

    def test_post_has_title(self):
        # Test that a Post object has the expected title
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')

    def test_post_has_content(self):
        # Test that a Post object has the expected content
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test post.')

class PostViewTest(TestCase):
    def setUp(self):
        # Create an Author object
        author = Author.objects.create(name='Test Author')
        # Create a Post object for testing views
        Post.objects.create(title='Test Post', content='This is a test post.', author=author)

    def test_post_list_view(self):
        # Test the post-list view
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        # Test the post-detail view
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post_detail', args=[str(post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')
    def test_can_create_a_new_post(self):
        response = self.client.post(
            reverse('post_create'),
            {'title': 'New Post', 'content': 'Created through the form.'},
        )
        self.assertRedirects(response, reverse('post_list'))
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_can_update_an_existing_post(self):
        post = Post.objects.get(id=1)
        response = self.client.post(
            reverse('post_update', args=[str(post.id)]),
            {'title': 'Updated Post', 'content': 'Updated content.'},
        )
        self.assertRedirects(response, reverse('post_list'))
        post.refresh_from_db()
        self.assertEqual(post.title, 'Updated Post')
        self.assertEqual(post.content, 'Updated content.')

    def test_can_delete_a_post(self):
        post = Post.objects.get(id=1)
        response = self.client.post(reverse('post_delete', args=[str(post.id)]))
        self.assertRedirects(response, reverse('post_list'))
        self.assertFalse(Post.objects.filter(id=post.id).exists())