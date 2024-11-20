import os
import pandas

# Read the storybooks CSV into a DataFrame, and write the DataFrame to a CSV file
videos_csv_url = 'https://raw.githubusercontent.com/elimu-ai/webapp/main/src/main/resources/db/content_PROD/eng/videos.csv'
print(os.path.basename(__file__), 'videos_csv_url: {}'.format(videos_csv_url))
videos_dataframe = pandas.read_csv(videos_csv_url)
print(os.path.basename(__file__), 'videos_dataframe: \n{}'.format(videos_dataframe))
videos_dataframe.to_csv('step1_videos.csv', index=False)

# Read the learning events CSV into a DataFrame, and write the DataFrame to a CSV file
video_learning_events_csv_url = 'http://eng.elimu.ai/analytics/video-learning-event/list/video-learning-events.csv'
print(os.path.basename(__file__), f'video_learning_events_csv_url: {video_learning_events_csv_url}')
video_learning_events_dataframe = pandas.read_csv(video_learning_events_csv_url)
print(os.path.basename(__file__), f'video_learning_events_dataframe: \n{video_learning_events_dataframe}')
video_learning_events_dataframe.to_csv('step1_video_learning_events.csv', index=False)
