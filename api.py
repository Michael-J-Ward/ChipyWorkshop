import meetup.api
client = meetup.api.Client('c725210249306a162b17454c27384c')

def get_meetup_members(event_id):
	rsvps = client.GetRsvps(event_id=event_id, urlname='_ChiPy_')
	member_id = ','.join([str(i['member']['member_id']) for i in rsvps.results])
	members = client.GetMembers(member_id=member_id)

	print(rsvps)
	print(member_id)
	print(members)

	for member in members.results:
	    try:
	    	yield member
	        #print('{0},{1},{2}'.format(member['name'], member['id'], member['photo']['thumb_link']))
	    except:
	        pass # ignore those who do not have a complete profile

# get_meetup_members('235484841')