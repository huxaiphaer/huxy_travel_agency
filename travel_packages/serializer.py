from rest_framework import serializers
from .models import TourPackages, Destinations


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = ['id', 'location', 'tour_type', 'danger_type']


class TourPackagesSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True)

    class Meta:
        model = TourPackages
        fields = ['id', 'name', 'description', 'price', 'capacity', 'destinations']

    def create(self, validated_data):
        destination_data = validated_data.pop('destinations')
        dest_obj_list = []
        for dest_data in destination_data:
            dest_obj = Destinations.objects.create(**dest_data)
            dest_obj_list.append(dest_obj)
        location = TourPackages.objects.create(**validated_data)
        location.destinations.set(dest_obj_list)
        location.save()
        return location

    # def update(self, instance, validated_data):
    #     destination_data = validated_data.pop("tour_destinations")
    #     destinations_all = (instance.tour_destinations).all()
    #     destinations_all = list(destinations_all)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.capacity = validated_data.get('capacity', instance.capacity)
    #     instance.save()
    #
    #     for dest in destination_data:
    #         d = destinations_all.pop(0)
    #         d.location = d.get('location', dest.location)
    #         d.tour_type = d.get('tour_type', dest.tour_type)
    #         d.danger_type = d.get('danger_type', dest.danger_type)
    #         d.save()
    #     return instance
