from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Aspirant, Test, Intresting
from .forms import PostForm, AspirantForm, TestForm, IntrestingForm

def stat_page1(request):
    return render(request, 'blog/page1.html')
def stat_page2(request):
    return render(request, 'blog/page2.html')
def stat_page3(request):
    return render(request, 'blog/page3.html')
def stat_page4(request):
    return render(request, 'blog/page4.html')
def stat_page5(request):
    return render(request, 'blog/page5.html')
def stat_aspirants(request):
    return render(request, 'blog/Aspirants.html')
def stat_anastasia(request):
    return render(request, 'blog/AnastasiaKolorova.html')
def book_anastasia(request):
    return render(request, 'blog/BookAnastasia.html')
def test_anastasia(request):
    return render(request, 'blog/TestAnastasia.html')
def intresting_list(request):
    intrestings = Intresting.objects.order_by('hierarchy')
    return render(request, 'blog/intresting_list.html', {'intrestings': intrestings})
def test_list(request):
    tests = Test.objects.order_by('hierarchy')
    return render(request, 'blog/test_list.html', {'tests': tests})
def aspirant_list(request):
    aspirants = Aspirant.objects.order_by('hierarchy')
    return render(request, 'blog/aspirant_list.html', {'aspirants': aspirants})
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse
    return render(request, 'blog/post_list.html', {'posts': posts})


def intresting_detail(request, pk):
    intresting = get_object_or_404(Intresting, pk=pk)
    return render(request, 'blog/intresting_detail.html', {'intresting': intresting})
def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'blog/test_detail.html', {'test': test})
def aspirant_detail(request, pk):
    aspirant = get_object_or_404(Aspirant, pk=pk)
    return render(request, 'blog/aspirant_detail.html', {'aspirant': aspirant})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def intresting_new(request):
    form = IntrestingForm()
    return render(request, 'blog/intresting_edit.html', {'form': form})
def test_new(request):
    form = TestForm()
    return render(request, 'blog/test_edit.html', {'form': form})
def aspirant_new(request):
    form = AspirantForm()
    return render(request, 'blog/aspirant_edit.html', {'form': form})
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def test_new(request):
    if request.method == "INTRESTING":
        form = IntrestingForm(request.INTRESTING)
        if form.is_valid():
            intresting = form.save(commit=False)
            intresting.save()
            return redirect('intresting_detail', pk=intresting.pk)
    else:
        form = IntrestingForm()
    return render(request, 'blog/intresting_edit.html', {'form': form})
def test_new(request):
    if request.method == "TEST":
        form = TestForm(request.TEST)
        if form.is_valid():
            test = form.save(commit=False)
            test.save()
            return redirect('test_detail', pk=test.pk)
    else:
        form = TestForm()
    return render(request, 'blog/test_edit.html', {'form': form})
def aspirant_new(request):
    if request.method == "ASPIRANT":
        form = AspirantForm(request.ASPIRANT)
        if form.is_valid():
            aspirant = form.save(commit=False)
            aspirant.save()
            return redirect('aspirant_detail', pk=aspirant.pk)
    else:
        form = AspirantForm()
    return render(request, 'blog/aspirant_edit.html', {'form': form})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def intresting_edit(request, pk):
    intresting = get_object_or_404(Intresting, pk=pk)
    if request.method == "INTRESTING":
        form = Intresting(request.INTRESTING, instance=intresting)
        if form.is_valid():
            intresting = form.save(commit=False)
            intresting.save()
            return redirect('intresting_detail', pk=intresting.pk)
    else:
        form = Intresting(instance=intresting)
    return render(request, 'blog/intresting_edit.html', {'form': form})
def test_edit(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == "TEST":
        form = TestForm(request.TEST, instance=test)
        if form.is_valid():
            test = form.save(commit=False)
            test.save()
            return redirect('test_detail', pk=test.pk)
    else:
        form = TestForm(instance=test)
    return render(request, 'blog/test_edit.html', {'form': form})
def aspirant_edit(request, pk):
    aspirant = get_object_or_404(Aspirant, pk=pk)
    if request.method == "ASPIRANT":
        form = AspirantForm(request.ASPIRANT, instance=aspirant)
        if form.is_valid():
            aspirant = form.save(commit=False)
            aspirant.author = request.user
            aspirant.published_date = timezone.now()
            aspirant.save()
            return redirect('aspirant_detail', pk=aspirant.pk)
    else:
        form = AspirantForm(instance=aspirant)
    return render(request, 'blog/aspirant_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

