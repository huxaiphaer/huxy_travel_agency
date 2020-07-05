from django.test import TestCase
from .models import TourPackages


class TourPackagesTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a tour package
        test_tour_package = TourPackages.objects.create(
            name='Germany tour', description='This tour ..', price=30.0, destinations='Koln, Frankfurt'
            , capacity=4
        )


    def test_tour_packages(self):

        tour_packages = TourPackages.get(id=1)
        name = f'{tour_packages.name}'
        description = f'{tour_packages.description}'
        price = f'{tour_packages.price}'
        destinations = f'{tour_packages.destinations}'
        capacity = f'{tour_packages.capacity}'

        self.assertEqual(name, 'Germany tour')
        self.assertEqual(description, 'This tour ..')
        self.assertEqual(price, 30.0)
        self.assertEqual(destinations, 'Koln, Frankfurt')
        self.assertEqual(capacity, 4)
