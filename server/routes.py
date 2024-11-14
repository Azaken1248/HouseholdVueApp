from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
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

    new_user = User(username=username, password=password,
                    role=role, email=email, phone=phone)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully!"}), 201


@api.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username, password=password).first()
    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
    }
    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, data=user_data), 200
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
    desc = request.json.get('type')
    date = request.json.get('date')
    time = request.json.get('time')
    amount = request.json.get('amount')

    new_request = ServiceRequest(user_id=user_id, service_id=service_id,
                                 status='pending', desc=desc, date=date, time=time, amount=amount)
    db.session.add(new_request)
    db.session.commit()
    return jsonify({"msg": "Service request created successfully!"}), 201


@api.route('/service-requests', methods=['GET'])
@jwt_required()
def get_service_requests():
    requests = ServiceRequest.query.all()
    return jsonify([{"id": req.id, "user_id": req.user_id, "service_id": req.service_id, "status": req.status, "service": req.desc} for req in requests])


@api.route('/service-requests/<int:request_id>/cancel', methods=['PATCH'])
@jwt_required()
def cancel_service_request(request_id):
    service_request = ServiceRequest.query.get(request_id)
    if not service_request:
        return jsonify({"msg": "Service request not found"}), 404
    service_request.status = 'canceled'
    db.session.commit()
    return jsonify({"msg": "Service request canceled successfully"}), 200


@api.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    users_data = [{"id": user.id, "username": user.username,
                   "email": user.email, "role": user.role} for user in users]
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


@api.route('/service-requests/professional', methods=['GET'])
@jwt_required()
def get_all_service_requests_for_professional():
    """
    Get all service requests available for the professional
    (status: 'pending', 'approved', 'denied').
    """
    current_user_id = get_jwt_identity()
    service_requests = ServiceRequest.query.filter_by(status='pending').all()
    return jsonify([
        {"id": req.id, "user_id": req.user_id, "service_id": req.service_id,
            "status": req.status, "service": req.desc, "date": req.date, "time": req.time}
        for req in service_requests
    ]), 200


@api.route('/service-requests/professional/approved', methods=['GET'])
@jwt_required()
def get_approved_service_requests_for_professional():
    """
    Get all service requests that the professional has approved (status: 'approved').
    """
    current_user_id = get_jwt_identity()  # Get the current logged-in user's ID
    service_requests = ServiceRequest.query.filter_by(status='approved').all()
    return jsonify([
        {"id": req.id, "user_id": req.user_id, "service_id": req.service_id,
            "status": req.status, "service": req.desc}
        for req in service_requests
    ]), 200


@api.route('/service-requests/professional/denied', methods=['GET'])
@jwt_required()
def get_denied_service_requests_for_professional():
    """
    Get all service requests that the professional has denied (status: 'denied').
    """
    current_user_id = get_jwt_identity()  # Get the current logged-in user's ID
    service_requests = ServiceRequest.query.filter_by(status='denied').all()
    return jsonify([
        {"id": req.id, "user_id": req.user_id, "service_id": req.service_id,
            "status": req.status, "service": req.desc}
        for req in service_requests
    ]), 200
