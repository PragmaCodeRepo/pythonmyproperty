# Generated by Django 4.1.7 on 2023-03-09 14:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_alter_bank_mortgaged'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='legal_representative',
        ),
        migrations.AddField(
            model_name='dealing',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='dealing',
            name='registeration_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Registeration Number'),
        ),
        migrations.AddField(
            model_name='dealing',
            name='value',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='original_amount',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Enter whole numbers.', regex='^[\\d\\,.]*$')], verbose_name='Original Loan Amount ($)'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='postal_state',
            field=models.CharField(blank=True, choices=[('ACT', 'ACT'), ('NSW', 'NSW'), ('NT', 'NT'), ('QLD', 'QLD'), ('SA', 'SA'), ('TAS', 'TAS'), ('VIC', 'VIC'), ('WA', 'WA'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='bathroom',
            name='bathroom_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='bedroom',
            name='ceiling_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='bedroom',
            name='curtains_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Other Features'),
        ),
        migrations.AlterField(
            model_name='bedroom',
            name='floors_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='bedroom',
            name='light_fittings_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='bedroom',
            name='walls_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='construction',
            name='external_walls',
            field=models.CharField(choices=[('Blue board', 'Blue board'), ('Brick', 'Brick'), ('Cladding - Metal', 'Cladding - Metal'), ('Cladding - Stone', 'Cladding - Stone'), ('Cladding - Vinyl', 'Cladding - Vinyl'), ('Cladding - Wood', 'Cladding - Wood'), ('Colourbond', 'Colourbond'), ('Concrete', 'Concrete'), ('Concrete Blocks', 'Concrete Blocks'), ('Fibre Cement', 'Fibre Cement'), ('Hardiplank', 'Hardiplank'), ('Render', 'Render'), ('Rendered - Bagged', 'Rendered - Bagged'), ('Stone', 'Stone'), ('Other', 'Other'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='External Walls'),
        ),
        migrations.AlterField(
            model_name='construction',
            name='external_walls_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='construction',
            name='foundation_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='construction',
            name='foundation_description',
            field=models.CharField(choices=[('Piers', 'Piers'), ('Pole', 'Pole'), ('Slab', 'Slab'), ('Other', 'Other'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Foundation'),
        ),
        migrations.AlterField(
            model_name='construction',
            name='roof_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='dealing',
            name='dealing_type',
            field=models.CharField(blank=True, choices=[('Caveat', 'Caveat'), ('Covenant', 'Covenant'), ('Easement', 'Easement'), ('Mortgage', 'Mortgage'), ('Other', 'Other'), ('Please Select', 'Please Select'), ('None', 'None')], default='Please Select', max_length=50, verbose_name='Dealing Type'),
        ),
        migrations.AlterField(
            model_name='dining',
            name='ceiling_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='dining',
            name='curtains_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='dining',
            name='floors_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='dining',
            name='light_fittings_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='dining',
            name='walls_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='ceiling',
            field=models.CharField(choices=[('None', 'None'), ('Gyprock', 'Gyprock'), ('Fibre Cement', 'Fibre Cement'), ('Timber', 'Timber'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Ceiling'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='ceiling_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='ceiling_condition',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Above Average', 'Above Average'), ('Average', 'Average'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='curtains_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='curtains_or_blinds',
            field=models.CharField(choices=[('None', 'None'), ('Blinds', 'Blinds'), ('Blinds-Aluminium', 'Blinds-Aluminium'), ('Blinds-Honeycomb', 'Blinds-Honeycomb'), ('Blinds-Mini', 'Blinds-Mini'), ('Blinds-Panel', 'Blinds-Panel'), ('Blinds-Pleated', 'Blinds-Pleated'), ('Blinds-Roller', 'Blinds-Roller'), ('Blinds-Sheer', 'Blinds-Sheer'), ('Blinds-Venetian', 'Blinds-Venetian'), ('Blinds-Vertical', 'Blinds-Vertical'), ('Curtains', 'Curtains'), ('Curtains-Box Pleated', 'Curtains-Box Pleated'), ('Curtains-Eyelet', 'Curtains-Eyelet'), ('Curtains-Goblet', 'Curtains-Goblet'), ('Curtains-Tailored Pleat', 'Curtains-Tailored Pleat'), ('Please Select', 'Please Select')], default='Blinds', max_length=50, verbose_name='Curtains/Blinds'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='floors',
            field=models.CharField(choices=[('None', 'None'), ('Carpet', 'Carpet'), ('Carpet-Pattern', 'Carpet-Pattern'), ('Carpet-Plain', 'Carpet-Plain'), ('Concrete', 'Concrete'), ('Cork', 'Cork'), ('Plastic', 'Plastic'), ('Plastic-Lino', 'Plastic-Lino'), ('Plastic-Vinyl', 'Plastic-Vinyl'), ('Stone', 'Stone'), ('Stone-Granite', 'Stone-Granite'), ('Stone-Limestone', 'Stone-Limestone'), ('Stone-Marble', 'Stone-Marble'), ('Stone-Sandstone', 'Stone-Sandstone'), ('Stone-Slate', 'Stone-Slate'), ('Stone-Travertine', 'Stone-Travertine'), ('Stone-Terrazzo', 'Stone-Terrazzo'), ('Tile', 'Tile'), ('Tile-Ceramic', 'Tile-Ceramic'), ('Tile-Mosaic', 'Tile-Mosaic'), ('Tile-Porcelain', 'Tile-Porcelain'), ('Tile-Wood', 'Tile-Wood'), ('Timber', 'Timber'), ('Timber-Floating Floor', 'Timber-Floating Floor'), ('Timber-Hardwood', 'Timber-Hardwood'), ('Timber-Polished', 'Timber-Polished'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Floors'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='floors_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='floors_condition',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Above Average', 'Above Average'), ('Average', 'Average'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='light_fittings',
            field=models.CharField(choices=[('None', 'None'), ('Track', 'Track'), ('Other', 'Other'), ('Chandelier', 'Chandelier'), ('Down Light', 'Down Light'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Light Fittings'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='light_fittings_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='walls',
            field=models.CharField(choices=[('None', 'None'), ('Brick', 'Brick'), ('Brick-Glass', 'Brick-Glass'), ('Fibre Cement', 'Fibre Cement'), ('Gyprock', 'Gyprock'), ('Picture Rails', 'Picture Rails'), ('Render', 'Render'), ('Tiles', 'Tiles'), ('Timber', 'Timber'), ('Wall Paper', 'Wall Paper'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Walls'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='walls_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='walls_condition',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Above Average', 'Above Average'), ('Average', 'Average'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='features',
            name='deck_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='features',
            name='deck_condition',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Above Average', 'Above Average'), ('Average', 'Average'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='features',
            name='deck_material',
            field=models.CharField(choices=[('Concrete', 'Concrete'), ('Timber', 'Timber'), ('Tiled', 'Tiled'), ('Other', 'Other'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Material'),
        ),
        migrations.AlterField(
            model_name='features',
            name='deck_present',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20, verbose_name='Deck Present'),
        ),
        migrations.AlterField(
            model_name='features',
            name='fencing_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='features',
            name='fencing_condition',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Above Average', 'Above Average'), ('Average', 'Average'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='features',
            name='fencing_material',
            field=models.CharField(choices=[('Brick', 'Brick'), ('Colourbond', 'Colourbond'), ('Timber', 'Timber'), ('Post & Wire', 'Post & Wire'), ('None', 'None'), ('Other', 'Other'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Material'),
        ),
        migrations.AlterField(
            model_name='features',
            name='pool_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='features',
            name='pool_condition',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Above Average', 'Above Average'), ('Average', 'Average'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='features',
            name='pool_material',
            field=models.CharField(choices=[('Concrete', 'Concrete'), ('Fibreglass', 'Fibreglass'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Material'),
        ),
        migrations.AlterField(
            model_name='features',
            name='pool_present',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20, verbose_name='Pool Present'),
        ),
        migrations.AlterField(
            model_name='features',
            name='registerd',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Registered'),
        ),
        migrations.AlterField(
            model_name='features',
            name='retaining_walls_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='features',
            name='retaining_walls_condition',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Above Average', 'Above Average'), ('Average', 'Average'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='features',
            name='retaining_walls_material',
            field=models.CharField(choices=[('None', 'None'), ('Blocks', 'Blocks'), ('Concrete', 'Concrete'), ('Sleepers', 'Sleepers'), ('Timber', 'Timber'), ('Treated Timber', 'Treated Timber'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Retaining Walls'),
        ),
        migrations.AlterField(
            model_name='grannyflat',
            name='granny_foundation_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='grannyflat',
            name='granny_roof_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='grannyflat',
            name='granny_walls_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='benchtops',
            field=models.CharField(choices=[('None', 'None'), ('Ceaser Stone', 'Ceaser Stone'), ('Concrete', 'Concrete'), ('Granite', 'Granite'), ('Laminated', 'Laminated'), ('Quartz', 'Quartz'), ('Stainless Steel', 'Stainless Steel'), ('Stone', 'Stone'), ('Timber', 'Timber'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Benchtops'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='cooktop',
            field=models.CharField(choices=[('None', 'None'), ('Electric', 'Electric'), ('Gas', 'Gas'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Cooktop'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='cooktop_ventilation',
            field=models.CharField(choices=[('None', 'None'), ('Exhaust Fan', 'Exhaust Fan'), ('Rangehood', 'Rangehood'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Cooktop Ventilation'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='cupboards',
            field=models.CharField(choices=[('None', 'None'), ('Laminated', 'Laminated'), ('Timber', 'Timber'), ('Polyurethane', 'Polyurethane'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Cupboards'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='oven_or_stove',
            field=models.CharField(choices=[('None', 'None'), ('Electric Upright', 'Electric Upright'), ('Gas Upright', 'Gas Upright'), ('Under Bench', 'Under Bench'), ('Wall Mount', 'Wall Mount'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Oven Or Stove'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='pantry',
            field=models.CharField(choices=[('None', 'None'), ('Built In', 'Built In'), ('Walk In', 'Walk In'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Pantry'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='sink',
            field=models.CharField(choices=[('None', 'None'), ('Single', 'Single'), ('1.25', '1.25'), ('1.50', '1.50'), ('Double', 'Double'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Sink'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='sink_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='splashback',
            field=models.CharField(choices=[('None', 'None'), ('Ceramic Tile', 'Ceramic Tile'), ('Glass', 'Glass'), ('Glass Mosaic', 'Glass Mosaic'), ('Stainless Steel', 'Stainless Steel'), ('Stone', 'Stone'), ('Other', 'Other'), ('Please Select', 'Please Select')], default='Please Select', max_length=50, verbose_name='Splashback'),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='laundry_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='lounge',
            name='balcony_present',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20, verbose_name='Balcony Present'),
        ),
        migrations.AlterField(
            model_name='lounge',
            name='ceiling_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='lounge',
            name='curtains_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='lounge',
            name='curtains_or_blinds',
            field=models.CharField(choices=[('None', 'None'), ('Blinds', 'Blinds'), ('Blinds-Aluminium', 'Blinds-Aluminium'), ('Blinds-Honeycomb', 'Blinds-Honeycomb'), ('Blinds-Mini', 'Blinds-Mini'), ('Blinds-Panel', 'Blinds-Panel'), ('Blinds-Pleated', 'Blinds-Pleated'), ('Blinds-Roller', 'Blinds-Roller'), ('Blinds-Sheer', 'Blinds-Sheer'), ('Blinds-Venetian', 'Blinds-Venetian'), ('Blinds-Vertical', 'Blinds-Vertical'), ('Curtains', 'Curtains'), ('Curtains-Box Pleated', 'Curtains-Box Pleated'), ('Curtains-Eyelet', 'Curtains-Eyelet'), ('Curtains-Goblet', 'Curtains-Goblet'), ('Curtains-Tailored Pleat', 'Curtains-Tailored Pleat')], default='None', max_length=50, verbose_name='Curtains/Blinds'),
        ),
        migrations.AlterField(
            model_name='lounge',
            name='floors_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='lounge',
            name='light_fittings_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='lounge',
            name='sliding_door_present',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20, verbose_name='Sliding Door Present'),
        ),
        migrations.AlterField(
            model_name='lounge',
            name='walls_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='carport',
            field=models.CharField(choices=[('None', 'None'), ('Single', 'Single'), ('Double', 'Double'), ('Tandem', 'Tandem'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Carport'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='carport_area',
            field=models.IntegerField(blank=True, null=True, verbose_name='Carport Area (m2)'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='garage',
            field=models.CharField(choices=[('None', 'None'), ('Single', 'Single'), ('Double', 'Double'), ('Tandem', 'Tandem'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Garage'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='garage_area',
            field=models.IntegerField(blank=True, null=True, verbose_name='Garage Area (m2)'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='other',
            field=models.CharField(choices=[('None', 'None'), ('Off Street', 'Off Street'), ('On Street', 'On Street'), ('Underground', 'Underground'), ('Other', 'Other'), ('Please Select', 'Please Select')], default='Please Select', max_length=100, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='parking_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bath',
            field=models.CharField(default=1, max_length=10, verbose_name='Bath'),
        ),
        migrations.AlterField(
            model_name='property',
            name='beds',
            field=models.CharField(default=1, max_length=10, verbose_name='Beds'),
        ),
        migrations.AlterField(
            model_name='property',
            name='garage',
            field=models.CharField(default=1, max_length=10, verbose_name='Garage'),
        ),
        migrations.AlterField(
            model_name='property',
            name='land',
            field=models.CharField(default=1, max_length=10, verbose_name='Land (m2)'),
        ),
        migrations.AlterField(
            model_name='property',
            name='number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='property',
            name='on_or_off_market',
            field=models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF')], default='ON', max_length=30, verbose_name='On Or Off Market'),
        ),
        migrations.AlterField(
            model_name='streetappeal',
            name='street_appeal_comments',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Comments'),
        ),
    ]