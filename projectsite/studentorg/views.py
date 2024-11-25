from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, Student, OrgMember, College, Program
from studentorg.forms import OrganizationForm, StudentForm, OrgMemberForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get("q")
            qs = qs.filter(Q(name__icontains=query)|Q(description__icontains=query))
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

# Student
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'stud_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query) |
                           Q(description__icontains=query))
        return qs

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'stud_add.html'
    success_url = reverse_lazy('student-list')


    def form_valid(self, form):
        form
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'stud_edit.html'
    success_url = reverse_lazy('student-list')


    def form_valid(self, form):
        form
        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'stud_del.html'
    success_url = reverse_lazy('student-list')


    def form_valid(self, form):
        messages.success(self.request, 'Successfully deleted.')
        return super().form_valid(form)


#Orgmember

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgm_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrgMemberList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get("q")
            qs = qs.filter(Q(student__lastname__icontains=query)|Q(student__firstname__icontains=query))
        return qs

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgm_add.html'
    success_url = reverse_lazy('orgmember-list')

    def form_valid(self, form):
        orgmember = form.instance
        messages.success(self.request, f'{orgmember} has been successfully added.')
        return super().form_valid(form)

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgm_edit.html'
    success_url = reverse_lazy('orgmember-list')

    def form_valid(self, form):
        orgmember = form.instance
        messages.success(self.request, f'{orgmember} has been successfully updated.')
        return super().form_valid(form)

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgm_del.html'
    success_url = reverse_lazy('orgmember-list')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully deleted.')
        return super().form_valid(form)

#Program
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'pro_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(ProgramList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get("q")
            qs = qs.filter(Q(prog_name__icontains=query)|Q(college__college_name__icontains=query))
        return qs

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'pro_add.html'
    success_url = reverse_lazy('program-list')

    def form_valid(self, form):
        program_name = form.instance.prog_name
        messages.success(self.request, f'{program_name} has been successfully added.')
        return super().form_valid(form)

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'pro_edit.html'
    success_url = reverse_lazy('program-list')

    def form_valid(self, form):
        prog_name = form.instance.prog_name
        messages.success(self.request, f'{prog_name} has been successfully updated.')
        return super().form_valid(form)

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'pro_del.html'
    success_url = reverse_lazy('program-list')


    def form_valid(self, form):
        messages.success(self.request, 'Successfully deleted.')
        return super().form_valid(form)


#College
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'col_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(CollegeList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get("q")
            qs = qs.filter(Q(college_name__icontains=query))
        return qs

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'col_add.html'
    success_url = reverse_lazy('college-list')

    def form_valid(self, form):
        college_name = form.instance.college_name
        messages.success(self.request, f'{college_name} has been successfully added.')
        return super().form_valid(form)


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'col_edit.html'
    success_url = reverse_lazy('college-list')


    def form_valid(self, form):
        college_name = form.instance.college_name
        messages.success(self.request, f'{college_name} has been successfully updated.')
        return super().form_valid(form)


class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'col_del.html'
    success_url = reverse_lazy('college-list')


    def form_valid(self, form):
        messages.success(self.request, 'Successfully deleted.')
        return super().form_valid(form)