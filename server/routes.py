from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from models import db, User, Service, ServiceRequest

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')
    email = request.json.get('email')
    phone = request.json.get('phone')
    
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already exists"}), 400
    
    new_user = User(username=username, password=password, role=role, email=email, phone=phone)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully!"}), 201


@api.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@api.route('/services', methods=['POST'])
@jwt_required()
def create_service():
    name = request.json.get('name')
    new_service = Service(name=name)
    db.session.add(new_service)
    db.session.commit()
    return jsonify({"msg": "Service created successfully!"}), 201

@api.route('/services', methods=['GET'])
@jwt_required()
def get_services():
    services = Service.query.all()
    return jsonify([{"id": service.id, "name": service.name} for service in services])

@api.route('/service-requests', methods=['POST'])
@jwt_required()
def create_service_request():
    user_id = request.json.get('user_id')
    service_id = request.json.get('service_id')
    
    new_request = ServiceRequest(user_id=user_id, service_id=service_id, status='pending')
    db.session.add(new_request)
    db.session.commit()
    return jsonify({"msg": "Service request created successfully!"}), 201

@api.route('/service-requests', methods=['GET'])
@jwt_required()
def get_service_requests():
    requests = ServiceRequest.query.all()
    return jsonify([{"id": req.id, "user_id": req.user_id, "service_id": req.service_id, "status": req.status} for req in requests])

@api.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    users_data = [{"id": user.id, "username": user.username, "email": user.email, "role": user.role} for user in users]
    return jsonify(users_data), 200
@api.route('/service-requests/<int:request_id>/approve', methods=['PATCH'])
@jwt_required()
def approve_service_request(request_id):
    service_request = ServiceRequest.query.get(request_id)
    if not service_request:
        return jsonify({"msg": "Service request not found"}), 404
    service_request.status = 'approved'
    db.session.commit()
    return jsonify({"msg": "Service request approved"}), 200

@api.route('/service-requests/<int:request_id>/deny', methods=['PATCH'])
@jwt_required()
def deny_service_request(request_id):
    service_request = ServiceRequest.query.get(request_id)
    if not service_request:
        return jsonify({"msg": "Service request not found"}), 404
    service_request.status = 'denied'
    db.session.commit()
    return jsonify({"msg": "Service request denied"}), 200
@api.route('/users/<int:user_id>', methods=['PATCH'])
@jwt_required()
def update_user_status(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    status = request.json.get('status')
    if status not in ['approved', 'blocked']:
        return jsonify({"msg": "Invalid status"}), 400

    user.status = status
    db.session.commit()
    return jsonify({"msg": f"User status updated to {status}"}), 200
