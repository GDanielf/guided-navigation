import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from roboflow import Roboflow
import cv2
import inference

class MultiCameraSubscriber(Node):
    def __init__(self):
        super().__init__('multi_camera_subscriber')

        self.image = None
        self.bridge = CvBridge()

        # Configuração do Modelo
        self.model = inference.get_model("husky_test/3")

        # Subscrições para os três tópicos de imagem
        self.subscription1 = self.create_subscription(
            Image,
            '/world/empty/model/rgbd_camera/link/link/sensor/camera_sensor/image',
            self.camera1_callback,
            10)
        
        self.subscription2 = self.create_subscription(
            Image,
            '/world/empty/model/rgbd_camera_1/link/link_1/sensor/camera_sensor_1/image',
            self.camera2_callback,
            10)
        
        self.subscription3 = self.create_subscription(
            Image,
            '/world/empty/model/rgbd_camera_2/link/link_2/sensor/camera_sensor_2/image',
            self.camera3_callback,
            10)
        
        self.subscription4 = self.create_subscription(
            Image,
            '/world/empty/model/rgbd_camera_3/link/link_3/sensor/camera_sensor_3/image',
            self.camera4_callback,
            10)        
        
        self.image = None
        # Desativar mensagens de retorno de chamada não utilizadas
        self.subscription1
        self.subscription2
        self.subscription3
        self.subscription4


    def camera1_callback(self, msg):
        self.get_logger().info('Recebida imagem da câmera 1')
        # Processamento da imagem da câmera 1
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        predict = self.model.infer(image = cv_image)
        print(predict)
        #predict_image = cv2.resize(predict, (640, 480))
        for prediction in predict[0].predictions:
            # Extrai as coordenadas e dimensões da caixa delimitadora
            x = int(prediction.x)
            y = int(prediction.y)
            width = int(prediction.width)
            height = int(prediction.height)
            
            # Calcula as coordenadas dos cantos da caixa
            top_left = (abs(int(width/2) - x), abs(int(height/2) - y))
            bottom_right = (int(width/2) + x, int(height/2) + y)
            
            # Desenha a caixa delimitadora na imagem
            cv2.rectangle(cv_image, top_left, bottom_right, (0, 255, 0), 2)  # Verde, espessura 2
        cv2.imshow('Camera 1', cv_image)
        cv2.waitKey(1)       

    def camera2_callback(self, msg):
        self.get_logger().info('Recebida imagem da câmera 2')
        # Processamento da imagem da câmera 2

    def camera3_callback(self, msg):
        self.get_logger().info('Recebida imagem da câmera 3')
        # Processamento da imagem da câmera 3

    def camera4_callback(self, msg):
        self.get_logger().info('Recebida imagem da câmera 4')
        # Processamento da imagem da câmera 4

def main(args=None):
    rclpy.init(args=args)
    node = MultiCameraSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()
