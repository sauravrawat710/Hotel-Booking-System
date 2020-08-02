from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from booking.forms import CustomUserCreationForm
from django.contrib.auth.models import Group
from booking.models import Hotel, Booking
from django.contrib import messages
from booking.forms import StaffForm

# Create your views here.


def home(request):
    if request.method == "POST":
        check_in = request.POST['indate']
        check_out = request.POST['outdate']
        guest = request.POST['guest']

        if not guest.isdigit():
            messages.error(request, 'Please Search for a valid No of Guests.')
            return redirect(home)

        case_1 = Booking.objects.filter(
            check_in__gte=check_in, check_out__lte=check_out).exists()

        if case_1:
            booking = Booking.objects.exclude(
                check_out__gte=check_out, check_out__lte=check_out).all()
            context = {
                'booking': booking
            }
            return render(request, 'users/home.html', context)

    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, 'users/home.html', context)


def dashboard(request):
    # for Customer side
    booking = Booking.objects.filter(guest=request.user).all()

    # for Staff side
    hotel = Hotel.objects.all()
    context = {
        'bookings': booking,
        'hotels': hotel,
    }
    return render(request, 'users/dashboard.html', context)


def update_dashboard(request, pk):
    # for Staff side

    if request.method == "POST":
        hotel = Hotel.objects.get(pk=pk)
        form = StaffForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Records Updated Successfully!')
            return redirect(dashboard)
    hotel = Hotel.objects.get(pk=pk)
    form = StaffForm(instance=hotel)
    context = {
        'form': form
    }
    return render(request, 'users/update_dash.html', context)


def booking(request, pk=None):
    if request.method == "POST":
        if pk:
            hotel = Hotel.objects.get(pk=pk)
            guest = request.user
            check_in = request.POST['check_in_date']
            check_out = request.POST['check_out_date']
            no_of_guest = request.POST['bookingGuest']

            if not no_of_guest.isdigit():
                messages.error(request, 'Please Enter valid No of Guests.')
                return redirect(home)

            # check wether the dates are valid
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Booking.objects.filter(
                hotel=hotel, check_in__lte=check_in, check_out__gte=check_in).exists()

            # case 2: a room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Booking.objects.filter(
                hotel=hotel, check_in__lte=check_out, check_out__gte=check_out).exists()

            case_3 = Booking.objects.filter(
                hotel=hotel, check_in__gte=check_in, check_out__lte=check_out).exists()

            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                messages.warning(
                    request, 'The room is not available on your selected dates')
                return redirect(home)

            # dates are valid
            booking = Booking(
                hotel=hotel,
                guest=guest,
                no_of_guest=no_of_guest,
                check_in=check_in,
                check_out=check_out,
            )

            booking.save()

            messages.success(
                request, 'Your Hotel has been Booked Successfully!')
            return redirect(dashboard)

        return render(request, 'users/home.html')


def customer_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password1']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            return redirect(home)
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/customer_signup.html', context)


def staff_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password1']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
            group = Group.objects.get(name='Staff')
            user.groups.add(group)
            return redirect(dashboard)
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/staff_signup.html', context)
