import cv2
import numpy as np
import tensorflow as tf
from PIL import ImageGrab
import matplotlib.pyplot as plt

class Sightseer(object):
	def __init__(self, filepath):
		self.filepath = filepath

	def render_grayscale(self, frame):
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		return gray_frame

	def load_webcam(self, return_data=True, set_gray=True, kill_key="q", width=160, height=120):

		cap = cv2.VideoCapture(0)
		cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
		cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

		frames = []

		while True:
			ret, frame = cap.read()
			print (frame.shape)

			if set_gray:
				frame = self.render_grayscale(frame)
			
			frame = cv2.flip(frame, 1) # prevent lateral inversion
			cv2.imshow('frame', frame)
			frames.append(frame)

			if cv2.waitKey(1) & 0xFF == ord(kill_key):
				break

		cap.release()
		cv2.destroyAllWindows()	

		if return_data:
			frames = np.array(frames)
			return frames
		
	def screen_grab(self, set_gray=True, write_data=True, return_data=True, kill_key="q", filename='output.avi', width=400, height=400):
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

		frames = []

		while True:
			img = np.array(ImageGrab.grab(bbox=(0, 0, width, height)))
			frame = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

			if write_data:
				out.write(imcv)

			if set_gray:
				frame = self.render_grayscale(img)

			cv2.imshow('frame', frame)
			frames.append(frame)

			if cv2.waitKey(1) & 0xFF == ord(kill_key):
				break

		out.release()
		cv2.destroyAllWindows()

		if return_data:
			frames = np.array(frames)
			return frames

	def load_source(self, return_data=True, set_gray=True, kill_key="q"):
		vidcap = cv2.VideoCapture(self.filepath)
		
		frame_exists, frame = vidcap.read()
		frames = []

		while frame_exists:
			frame_exists, frame = vidcap.read()
			print (frame.shape)

			if set_gray:
				frame = self.render_grayscale(frame)

			cv2.imshow('frame', frame)
			frames.append(frame)

			if cv2.waitKey(1) & 0xFF == ord(kill_key):
				break
		
		vidcap.release()
		cv2.destroyAllWindows()
		
		if return_data:
			frames = np.array(frames)
			return frames

	def load_image(self):
		try:
			img = cv2.imread(self.filepath)
			return img
		except:
			raise FileExistsError ("File does not exist. You may want to check the filepath again.")

	def write_img(self, image, image_path):
		image_path = image_path.split('/')
		img_name = image_path[-1]
		img_name = img_name.split('.')
		img_name = img_name[0] + "_detected." + img_name[1]
		image_path = "/".join(image_path[:-1]) + "/" + img_name

		print ('Saved edited image at {}'.format(image_path))

		cv2.imwrite(image_path, (image).astype('uint8'))	
	
	# def render_image(self, image, boxes, save_img=True, random_coloring=True):
	# 	for box in boxes:
	# 		label_str = box[0]
	# 		confidence = box[1]
	# 		coords = box[2]

	# 		if random_coloring:
	# 			r = np.random.randint(0, 255)
	# 			g = np.random.randint(0, 255)
	# 			b = np.random.randint(0, 255)
	# 		else:
	# 			r = 0
	# 			g = 255
	# 			b = 0

	# 		cv2.rectangle(image, (coords['xmin'], coords['ymin']), (coords['xmax'], coords['ymax']), (r, g, b), 3)
	# 		cv2.putText(image, '{}: {:.3f}'.format(label_str, confidence), (coords['xmax'], coords['ymin']-13), cv2.FONT_HERSHEY_SIMPLEX, 1e-3 * image.shape[0], (r, g, b), 2)

	# 	image = np.squeeze(image)
	# 	image = image.astype('uint8')
	# 	image = image / 255
		
	# 	print (image.shape)

	# 	if save_img:
	# 		self.write_img(image, self.filepath)

	# 	plt.imshow(image)
	# 	plt.show()
	
	# 	return image

	def render_image(self, img):
		plt.imshow(img)
		plt.show()