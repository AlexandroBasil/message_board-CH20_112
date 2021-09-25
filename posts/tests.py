from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="A test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, "A test")


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Another test")

    def test_homepage_uses_correct_model(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Another test")

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, "post_list.html")

    def test_view_extends_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, "base.html")

    
class DetailPageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="One more test")

    def test_postdetail_page_uses_correct_model(self):
        response = self.client.get(reverse('post_detail', args=[1]))
        self.assertContains(response, "One more test")
    
    def test_postdetail_view_url_exists_at_proper_location(self):
        response = self.client.get(('/posts/1/'))
        self.assertEqual(response.status_code, 200)
    
    def test_postdetail_view_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[1]))

    def test_postdetail_view_uses_correct_template(self):
        response = self.client.get(reverse('post_detail', args=[1]))
        self.assertTemplateUsed(response, "post_detail.html")

    def test_postdetail_view_extends_correct_template(self):
        response = self.client.get(reverse('post_detail', args=[1]))
        self.assertTemplateUsed(response, "base.html")