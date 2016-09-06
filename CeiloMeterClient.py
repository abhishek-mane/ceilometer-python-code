'''
    This python file contains code responsible for talking to the ceilometer.
    includes
    1. establishing connection
    2. making query
    3. & getting executed the query in ceilometer environment
    Returns the List of Dicts as output
'''
import ceilometerclient.client

class CeiloMeterClient:
    CEILOMETER_API_VERSION = "2"

    def __init__(self, inputData):
        self.credentials = inputData['credentials']
        self.filter = inputData['filter']
        try:
            self.cclient = ceilometerclient.client.get_client(
                                            CeiloMeterClient.CEILOMETER_API_VERSION,
                                            os_username=self.credentials['username'],
                                            os_password=self.credentials['password'],
                                            os_tenant_name=self.credentials['tenant_name'],
                                            os_auth_url=self.credentials['auth_url'],
                                            os_user_domain_id=self.credentials['user_domain_id'],
                                            os_project_domain_id=self.credentials['project_domain_id']
                                        )
        except Exception, err:
            print "Error while enstablishing connection...", err

    def makeQuery(self):
        query = []
        if self.filter['user_id']:
            query.append({"field": "user_id", "op": "eq", "value": self.filter['user_id']})
        if self.filter['tenant_id']:
            query.append({"field": "project_id", "op": "eq", "value": self.filter['tenant_id']})
        if self.filter['timestamp_low_limit']:
            query.append({"field": "timestamp", "op": "ge", "value": self.filter['timestamp_low_limit']})
        if self.filter['timestamp_high_limit']:
            query.append({"field": "timestamp", "op": "le", "value": self.filter['timestamp_high_limit']})
        return query

    def query(self):
        listOfMeters = []
        query = self.makeQuery()
        for meter in self.filter['meter']:
            row = eval(
                        str(self.cclient.statistics.list(meter, query)).replace("[<Statistics", "").replace(">]", "")
                  )
            row['meter'] = meter
            listOfMeters.append(row)

        return listOfMeters
