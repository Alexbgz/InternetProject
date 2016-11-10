from django.shortcuts import render
from django.http import Http404
from django.views import View
from lab.example import posts, posts_dict


def main(request):
    return render(request, 'main.html', {
        'posts': posts
    })

class PostView(View):
    def get(self, request, id):
        post = posts_dict.get(int(id))

        if post is None:
            raise Http404

        return render(request, 'post.html', {
            'post': post
        })
