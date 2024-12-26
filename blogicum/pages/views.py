from django.shortcuts import render


def about(request):
    """View функция - раздел 'О проекте'."""
    template = 'pages/about.html'
    return render(
        request=request,
        template_name=template,
    )


def rules(request):
    """View функция - раздел 'Наши правила'."""
    template = 'pages/rules.html'
    return render(
        request=request,
        template_name=template,
    )
