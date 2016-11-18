import meetup.api
client = meetup.api.Client('c725210249306a162b17454c27384c')

rsvps=client.GetRsvps(event_id='235484841', urlname='_ChiPy_')
member_id = ','.join([str(i['member']['member_id']) for i in rsvps.results])
members = client.GetMembers(member_id=member_id)

for member in members.results:
    try:
        print('{0},{1},{2}'.format(member['name'], member['id'], member['photo']['thumb_link']))
    except:
        pass # ignore those who do not have a complete profile