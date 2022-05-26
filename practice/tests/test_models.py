from django.test import TestCase
from ..models import *

class ModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def test_person_make_id_automatically(self):
        Person.objects.create(first_name='Big', last_name='Bob')
        person = Person.objects.get(id=1)

        self.assertEqual('Big', person.first_name)

    def test_person_save(self):
        f_name = 'Big'
        l_name = 'Bob'
        person = Person(first_name=f_name, last_name=l_name)
        person.save()

        self.assertEqual(Person.objects.get(id = 1).first_name,f_name)
        self.assertEqual(Person.objects.get(id = 1).last_name,l_name)

    def test_shirt_size_of_customer_should_be_Large(self):
        Person.objects.create(first_name='Big', last_name='Bob')
        p = Person.objects.get(id=1)
        Customer.objects.create(person=p, shirt_size='L')
        customer = Customer.objects.get(id = 1)

        self.assertEqual(customer.get_shirt_size_display(), 'Large')

    def test_blog_and_entry_model_is_one_to_many_relationship(self):
        Blog.objects.create(name = 'blog name')
        b = Blog.objects.get(id=1)
        Comment.objects.create(blog=b, content='content1')
        Comment.objects.create(blog=b, content='content2')

        self.assertEqual(Comment.objects.get(id = 1).blog, Comment.objects.get(id=2).blog)

    def test_blog_alreay_saved_should_be_update(self):
        # save
        n = 'blog name'
        b = Blog(name = n)
        b.save()
        self.assertEqual(b.name, n)

        # update
        new_n = 'New name'
        b.name = new_n
        b.save()
        self.assertEqual(b.name, new_n)

    def test_return_queryset_that_contains_all_comments_objects(self):
        b = Blog(name='blog name')
        c1 = Comment(blog=b, content='content1')
        c2 = Comment(blog=b, content='content2')
        b.save()
        c1.save()
        c2.save()

        print(Comment.objects.all())

    def test_return_specific_object_with_filter(self):
        b = Blog(name='blog name')
        c1 = Comment(blog=b, content='content1')
        c2 = Comment(blog=b, content='content2')
        b.save()
        c1.save()
        c2.save()

        f1 = Comment.objects.filter(content='content1')
        f2 = Comment.objects.filter(content__startswith='content')
        print(f1)
        print(f2)

    def test_return_one_single_object_with_get(self):
        b = Blog(name='blog name')
        c1 = Comment(blog=b, content='content1')
        c2 = Comment(blog=b, content='content2')
        b.save()
        c1.save()
        c2.save()

        comment_get_by_column = Comment.objects.get(content='content1')
        comment_get_by_pk = Comment.objects.get(pk = 1)

        self.assertEqual(comment_get_by_pk, comment_get_by_column)


    def test_raise_does_not_exist_if_there_are_no_results_that_match_the_query(self):

        with self.assertRaises(Comment.DoesNotExist):
            comment = Comment.objects.get(content='content22222')

    def test_raise_multiple_object_returned_if_there_are_a_lot_of_result_that_match_the_query(self):
        b = Blog(name='blog name')
        c1 = Comment(blog=b, content='content1')
        c2 = Comment(blog=b, content='content1')
        b.save()
        c1.save()
        c2.save()

        with self.assertRaises(Comment.MultipleObjectsReturned):
            comment = Comment.objects.get(content='content1')

    def test_query(self):
        b = Blog(name='blog name')
        c1 = Comment(blog=b, content='content1')
        c2 = Comment(blog=b, content='content2')
        c3 = Comment(blog=b, content='content3')
        c4 = Comment(blog=b, content='content4')
        c5 = Comment(blog=b, content='content5')
        c6 = Comment(blog=b, content='content6')
        c7 = Comment(blog=b, content='content7')
        c8 = Comment(blog=b, content='content8')
        c9 = Comment(blog=b, content='content9')
        c10 = Comment(blog=b, content='content10')
        b.save()
        c1.save()
        c2.save()
        c3.save()
        c4.save()
        c5.save()
        c6.save()
        c7.save()
        c8.save()
        c9.save()
        c10.save()

        # limit 5
        print(Comment.objects.all()[:5])

        # offset 5 limit 5
        print(Comment.objects.all()[5:10])

        # order by content limit 1
        print(Comment.objects.order_by('content')[0])

        # SELECT * FROM blog_comment WHERE content = 'content10';
        print(Comment.objects.get(content__exact='content10'))

        # SELECT * FROM blog_comment WHERE content LIKE '%content';
        print(Comment.objects.get(content__contains='content10'))

        # JOIN
        # SELECT * FROM blog_comment JOIN blog ON blog.id = comment.blog_id
        # WHERE blog_name = 'blog_name';
        print(Comment.objects.filter(blog__name='blog name'))

        # SELECT * FROM blog_comment JOIN blog ON blog.id = comment.blog_id
        # WHERE blog_name LIKE '%blog_name';
        print(Comment.objects.filter(blog__name__contains='blog name'))












