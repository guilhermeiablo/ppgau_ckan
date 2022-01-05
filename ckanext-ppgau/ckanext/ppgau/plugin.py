# encoding: utf-8

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit




def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        data_dict={'sort': 'package_count desc', 'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    groups = groups[:10]

    return groups


class PpgauPlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    plugins.implements(plugins.IFacets)

    def dataset_facets(self, facets_dict, package_type):
        facets_dict['municipio'] = toolkit._('Município')
        facets_dict['estado'] = toolkit._('Estado')
        facets_dict['extent'] = toolkit._('Abrangência')
        facets_dict['database'] = toolkit._('Base de dados')
        facets_dict['date'] = toolkit._('Ano')
        # Return the updated facet dict.
        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        facets_dict['groups'] = toolkit._('Grupos')
        facets_dict['municipio'] = toolkit._('Município')
        facets_dict['estado'] = toolkit._('Estado')
        facets_dict['extent'] = toolkit._('Abrangência')
        facets_dict['database'] = toolkit._('Base de dados')
        facets_dict['date'] = toolkit._('Ano')
        return facets_dict

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')
    

    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''

        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'ppgau_most_popular_groups': most_popular_groups}
