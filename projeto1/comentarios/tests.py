from django.test import TestCase
from .models import Comentario


class SalvarComentarioViewTests(TestCase):
    def test_homepage_renders_comment_form(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enviar Comentário')
        self.assertContains(response, 'Nenhum comentário disponível.')

    def test_post_saves_comment_and_displays_it_after_redirect(self):
        response = self.client.post(
            '/',
            {'autor': 'Ana', 'texto': 'Meu comentário'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comentario.objects.count(), 1)
        self.assertContains(response, 'Ana: Meu comentário')
