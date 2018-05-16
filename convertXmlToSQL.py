# XML Daten so verarbeiten das Sie in der Datenbank eingelesen werden kann
# Auswahl der Datenbank für große Daten

from xml.etree.ElementTree import iterparse
from bs4 import BeautifulSoup
import sqlite3


def processingUsersXML(element):
    #! Id
    # Reputation
    # CreationDate
    # DisplayName
    # LastAccessDate
    # WebsiteUrl
    # Location
    # AboutMe
    # Views
    # UpVotes
    # DownVotes
    # AccountId
    # Age
    #! ProfileImageURL 



    # Brauch ich die ID
    #print("Id:"+element['Id'])
    #print("Reputation:"+element['Reputation'])
    #print("CreationDate:"+element['CreationDate'])
    #print("DisplayName:"+element['DisplayName'])
    #print("LastAccessDate:"+element['LastAccessDate'])
        
    #print("WebsiteUrl:"+str(element['WebsiteUrl']))
    
    
    #print("Location:"+element['Location'])
    if element.get('Location') is None:
        element = {'Location':'None'}
    
    print(element['Location'])

    # Validation for AboutMe
    # Removing HTML Tags from Strings
    if element.get('AboutMe') is not None:
        cleanAboutMe = BeautifulSoup(element['AboutMe'], "lxml").text
        element['AboutMe'] = cleanAboutMe
    else:
        element = {'AboutMe':'None'}
        

    
    
    #print("AboutMe:"+element['AboutMe'])

    
    #print("Views:"+element['Views'])
    #print("UpVotes:"+element['UpVotes'])
    #print("DownVotes:"+element['DownVotes'])
    #print("AccountId:"+element['AccountId'])
    #Age
    #ProfileImageURL

    return "0"

def processingBadgesXML(element):
   # Id
   # UserId
   # Name
   #! Date
   # Class
   # TagBased
    return 0

def processingCommentsXML(element):
   # Id
   # PostId
   # Score
   # Text
   # CreationDate
   # UserId
    return 0

def processingPostHistoryXML(element):
   # Id
   # PostHistoryTypeId
   # PostId
   #! RevisionGUID
   # CreationDate
   # UserId
   # Text
    return 0

def processingPostsXML(element):
   # Id
   # PostTypeId
   # AcceptedAnswerId
   # CreationDate
   # Score
   #! ViewCount
   # Body
   # OwnerUserId
   #! LastEditorUserId
   #! LastEditorDisplayName
   #! LastEditDate
   #! LastActivityDate
   # Title
   # Tags
   # AnswerCount
   #! CommentCount
   # FavoriteCount
   #! CommunityOwnedDate
    return 0

def processingTagsXML(element):
   # Id
   # TagName
   # Count
   #! ExcerptPostId
   #! WikiPostId
    return 0


def savingDataToDatabase(databaseName, element):
    return 0

#? Der Name gefaellt mir nicht
def processingDataForSQL(filename, element):
    if filename == 'Users':
        user = processingUsersXML(element)
        savingDataToDatabase(filename, user)

    elif filename == 'Badges':
        badges = processingBadgesXML(element)
        savingDataToDatabase(filename, badges)

    elif filename == 'Comments':
        comments = processingCommentsXML(element)
        savingDataToDatabase(filename, comments)

    elif filename == 'PostHistory':
        postHistory = processingPostHistoryXML(element)
        savingDataToDatabase(filename, postHistory)

    

    elif filename == 'Posts':
        posts = processingPostsXML(element)
        savingDataToDatabase(filename, posts)
    elif filename == 'Tags':
        tags = processingTagsXML(element)
        savingDataToDatabase(filename, tags)
    
    else:
        print("Leider ist ein Fehler aufgetaucht.\n"+
        "Bitte Beachten Sie das wir 8 Dateinamen haben die das Programm erkennt\n"+
        "Users, Badges, Comments, PostHistory, PostHistory, PostLinks, Posts, Tags, Votes")
        return False
        
        


def getDataFromXml(filename):
    for evt, elem in iterparse('/../usws/stackoverflowDataScience/dumpData/'+str(filename)+'.xml', events=('end',)):
        if elem.tag == 'row':
            user_fields = elem.attrib
            #print(user_fields)
            processingDataForSQL(filename, user_fields)

            
            #if user_fields['DisplayName'] == 'Anonymous User':
            #    break


           

            



def chosenXMLFile():
    getDataFromXml('Users')
    #getDataFromXml('Badges')
    #getDataFromXml('Comments')
    #getDataFromXml('PostHistory')
    #getDataFromXml('Posts')
    #getDataFromXml('Tags')
    

chosenXMLFile()