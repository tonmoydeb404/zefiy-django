from django.shortcuts import render

servicesList = [
    {
        "id": "01",
        "icon": "laptop_mac",
        "title": "Web Development",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbiac faucibus non netus est, egestas elit.",
    },
    {
        "id": "02",
        "icon": "developer_mode",
        "title": "App Development",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbiac faucibus non netus est, egestas elit.",
    },
    {
        "id": "03",
        "icon": "donut_large",
        "title": "Digital Marketing",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbiac faucibus non netus est, egestas elit.",
    },
    {
        "id": "04",
        "icon": "lock",
        "title": "Security Service",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbiac faucibus non netus est, egestas elit.",
    },
    {
        "id": "05",
        "icon": "query_stats",
        "title": "SEO",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbiac faucibus non netus est, egestas elit.",
    },
    {
        "id": "06",
        "icon": "draw",
        "title": "UI UX",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbiac faucibus non netus est, egestas elit.",
    },
    {
        "id": "07",
        "icon": "dashboard",
        "title": "ERP Software",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbiac faucibus non netus est, egestas elit.",
    },
    {
        "id": "08",
        "icon": "manage_accounts",
        "title": "Brand Manager",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbiac faucibus non netus est, egestas elit.",
    }
]


def home(request):
    context = {
        "services": servicesList[:4],
        "page_title": "zeFiy - your digital agency"
    }
    return render(request, 'website/home.html', context)


def about(request):
    context = {
        "page_title": "About us - zeFiy"
    }
    return render(request, 'website/about.html', context)


def services(request):
    context = {
        "services": servicesList,
        "page_title": "Our Services - zeFiy"
    }
    return render(request, 'website/services.html', context)
