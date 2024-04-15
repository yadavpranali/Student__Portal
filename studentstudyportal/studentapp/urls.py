from django.urls import path
from studentapp import views

urlpatterns = [
    path('home',views.home),
    path('notes',views.notes),
    path('delete_note/<int:pk>',views.delete_note,name='delete-note'),

    #path('delete_note/<int:pk>',views.delete_note,name='delete-note'),
    #path('delete/<rid>',views.delete_note),
    #path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name='notes-detail'),
    path('note_details/<int:pk>',views.Note_details,name='note_details'),
    path('homework',views.homework,name='homework'),
    path('update_homework/<int:pk>',views.update_homework,name=
    'update-homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name='delete-homework'),
    path('youtube',views.youtube,name='youtube'),
    path('todo',views.todo,name='todo'),
    path('update_todo/<int:pk>',views.update_todo,name=
    'update-todo'),
    path('delete_todo/<int:pk>',views.delete_todo,name='delete-todo'),
    path('books',views.books,name='books'),
    path('dictionary',views.dictionary,name='dictionary'),
    path('wiki',views.wiki,name='wiki'),
    path('conversion',views.conversion,name='conversion'),


]

