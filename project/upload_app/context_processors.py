def auth_status(request):
    if request.user.is_authenticated:
        return {'is_authenticated': True}
    else:
        return {'is_authenticated': False}

