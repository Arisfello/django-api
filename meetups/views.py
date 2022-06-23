from django.shortcuts import render


def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'Location': 'Naivasha',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A Second Meetup',
            'Location': 'Nairobi',
            'slug': 'a-Second-meetup'
        },
        {
            'title': 'A Third Meetup',
            'Location': 'Mombasa',
            'slug': 'a-Third-meetup'
        },
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request):
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup!'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']

    })
