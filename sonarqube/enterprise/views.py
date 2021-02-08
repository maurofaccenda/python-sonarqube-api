from sonarqube.utils.common import POST, GET
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_VIEWS_UPDATE,
    API_VIEWS_SHOW,
    API_VIEWS_SET_TAGS_MODE,
    API_VIEWS_SET_REMAINING_PROJECTS_MODE,
    API_VIEWS_SET_REGEXP_MODE,
    API_VIEWS_SET_MANUAL_MODE,
    API_VIEWS_REMOVE_PROJECT,
    API_VIEWS_MOVE_OPTIONS,
    API_VIEWS_MOVE,
    API_VIEWS_LOCAL_VIEWS,
    API_VIEWS_LIST,
    API_VIEWS_DEFINITION,
    API_VIEWS_DEFINE,
    API_VIEWS_CREATE,
    API_VIEWS_ADD_SUB_VIEW,
    API_VIEWS_ADD_PROJECT,
    API_VIEWS_ADD_LOCAL_VIEW
)


class SonarViews(RestClient):
    """
    Manage Portfolios
    """

    special_attributes_map = {"definition": "def"}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarViews, self).__init__(**kwargs)

    def get(self, key):
        result = self.list()
        for view in result["views"]:
            if view["key"] == key:
                return view

    @POST(API_VIEWS_ADD_LOCAL_VIEW)
    def add_local_view(self, key, ref_key):
        """
        POST api/views/add_local_view
        since 1.0
        Add a local reference to an existing portfolio
        Authentication is required for this API endpoint

            Parameters

        key
        required

        Key of the parent portfolio

        ref_key
        required

        Key of the referenced local portfolio
        """

    @POST(API_VIEWS_ADD_PROJECT)
    def add_project(self, key, project):
        """
        POST api/views/add_project
        since 1.0
        Add a project to a portfolio
        Requires 'Administrator' permission on the portfolio and 'Browse' permission for adding project

            Parameters
            Changelog

        key
        required

        Key of the portfolio

        project
        required

        Key of the project

        Example value
        my_project
        """

    @POST(API_VIEWS_ADD_SUB_VIEW)
    def add_sub_view(self, key, name, description=None, subKey=None):
        """
        POST api/views/add_sub_view
        since 1.0
        Add a portfolio to an existing portfolio
        Authentication is required for this API endpoint

            Parameters
            Changelog

        description
        optional

        Description of the new portfolio, can be left blank

        Maximum length
        256
        key
        required

        Key of the parent portfolio

        name
        required

        Name of the new portfolio

        Maximum length
        256
        subKey
        optional

        If specified, will be used for the new portfolio's key instead of the default generated value

        Maximum length
        400
        """

    @POST(API_VIEWS_CREATE)
    def create(self, name, description=None, key=None, visibility=None):
        """
        POST api/views/create
        since 1.0
        Create a new (root) portfolio.
        Requires 'Administer System' permission or 'Create Portfolios' permission

            Parameters
            Changelog

        description
        optional

        Description for the new portfolio, can be left blank

        Maximum length
        256
        key
        optional

        Key for the new portfolio. A suitable key will be generated if not provided

        Maximum length
        400
        name
        required

        Name for the new portfolio

        Maximum length
        256
        visibility
        optional
        since 2.0

        Whether the created portfolio or application should be visible to everyone, or only specific user/groups.
        If no visibility is specified, the default visibility of the organization will be used.

        Possible values

            private
            public
        """

    @POST(API_VIEWS_DEFINE)
    def define(self, definition):
        """
        POST api/views/define
        since 1.0
        Define the portfolio structure by uploading a XML definition file. The uploaded file is validated against the
        XML Schema available on the server and its structure is checked for inconsistencies (e.g loops in local
        references, duplicate project associations). If the file is deemed valid, the portfolio hierarchy is updated
        according to the contents of the file. Requires Provision Projects permission.

            Parameters

        def
        required

        XML file to upload and validate
        """

    @GET(API_VIEWS_DEFINITION)
    def definition(self):
        """
        GET api/views/definition
        since 2.0
        Return the definition of the structure of portfolios in XML format. Requires Create Projects permission.
        """

    @POST("/api/views/delete")
    def delete(self, key):
        """
        POST api/views/delete
        since 1.0
        Delete a portfolio definition
        .Requires 'Administrator' permission on the portfolio

            Parameters
            Changelog

        key
        required

        Portfolio key
        """

    @GET(API_VIEWS_LIST)
    def list(self):
        """
        GET api/views/list
        since 1.0
        List root portfolios.
        Requires authentication. Only portfolios with the admin permission are returned.

            Response Example
            Changelog

        {
          "views": [
            {
              "key": "apache-jakarta-commons",
              "name": "Apache Jakarta Commons",
              "qualifier": "VW",
              "visibility": "public"
            },
            {
              "key": "Languages",
              "name": "Languages",
              "qualifier": "VW",
              "visibility": "private"
            },
            {
              "key": "SonarQube_Ecosystem",
              "name": "SonarQube Ecosystem",
              "qualifier": "APP",
              "visibility": "public"
            }
          ]
        }
        """

    @GET(API_VIEWS_LOCAL_VIEWS)
    def local_views(self, key):
        """
        GET api/views/local_views
        since 1.0
        List portfolios that can be locally referrenced
        Authentication is required for this API endpoint

            Parameters
            Response Example

        key
        required

        Key of the would-be parent portfolio
        """

    @POST(API_VIEWS_MOVE)
    def move(self, destination, key):
        """
        POST api/views/move
        since 1.0
        Move a portfolio
        Authentication is required for this API endpoint

            Parameters

        destination
        required

        Key of the destination portfolio

        key
        required

        Key of the portfolio to move
        """

    @GET(API_VIEWS_MOVE_OPTIONS)
    def move_options(self, key):
        """
        GET api/views/move_options
        since 1.0
        List possible portfolio destinations
        Authentication is required for this API endpoint

            Parameters
            Response Example

        key
        required

        Key of the portfolio to move
        """

    @POST(API_VIEWS_REMOVE_PROJECT)
    def remove_project(self, key, project):
        """
        POST api/views/remove_project
        since 1.0
        Remove a project from a portfolio
        Requires 'Administrator' permission on the portfolio

            Parameters
            Changelog

        key
        required

        Key of the portfolio

        project
        required

        Key of the project
        """

    @POST(API_VIEWS_SET_MANUAL_MODE)
    def set_manual_mode(self, portfolio):
        """
        POST api/views/set_manual_mode
        since 7.4
        Set the projects selection mode of a portfolio on manual selection.
        In order to add project, please use api/view/add_project.
        Requires 'Administrator' permission on the portfolio

            Parameters

        portfolio
        required

        Key of the portfolio or sub-portfolio to update
        """

    @POST(API_VIEWS_SET_REGEXP_MODE)
    def set_regexp_mode(self, portfolio, regexp):
        """
        POST api/views/set_regexp_mode
        since 7.4
        Set the projects selection mode of a portfolio on regular expression.
        Requires 'Administrator' permission on the portfolio

            Parameters

        portfolio
        required

        Key of the portfolio or sub-portfolio to update

        regexp
        required

        A valid regexp with respect to the JDK's ``java.util.regex.Pattern`` class
        """

    @POST(API_VIEWS_SET_REMAINING_PROJECTS_MODE)
    def set_remaining_projects_mode(self, portfolio):
        """
        POST api/views/set_remaining_projects_mode
        since 7.4
        Set the projects selection mode of a portfolio on unassociated projects in hierarchy.
        Requires 'Administrator' permission on the portfolio

            Parameters

        portfolio
        required

        Key of the portfolio or sub-portfolio to update
        """

    @POST(API_VIEWS_SET_TAGS_MODE)
    def set_tags_mode(self, portfolio, tags):
        """
        POST api/views/set_tags_mode
        since 7.4
        Set the projects selection mode of a portfolio on project tags.
        Requires 'Administrator' permission on the portfolio

            Parameters

        portfolio
        required

        Key of the portfolio or sub-portfolio to update

        tags
        required

        Comma-separated list of tags. It's not possible to set nothing.
        """

    @GET(API_VIEWS_SHOW)
    def show(self, key):
        """
        GET api/views/show
        since 1.0
        Show the details of a portfolio, including its hierarchy and project selection mode.
        Authentication is required for this API endpoint

            Parameters
            Response Example
            Changelog

        key
        required

        The key of the portfolio
        """

    @POST(API_VIEWS_UPDATE)
    def update(self, key, name, description=None):
        """
        POST api/views/update
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

            Parameters
            Changelog

        description
        optional

        New description for the application

        Maximum length
        256
        key
        required

        Key of the portfolio to update

        name
        required

        New name for the portfolio

        Maximum length
        256
        """