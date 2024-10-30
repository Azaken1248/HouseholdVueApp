<template>
  <div class="container mt-5">
    <h2>Admin Dashboard</h2>
    <div class="row">
      <div class="col-md-6">
        <h3>Manage Users</h3>
        <table class="table">
          <thead>
            <tr>
              <th>Username</th>
              <th>Email</th>
              <th>Role</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id">
              <td>{{ user.username }}</td>
              <td>{{ user.email }}</td>
              <td>{{ user.role }}</td>
              <td>
                <button class="btn btn-warning btn-sm">Block</button>
                <button class="btn btn-success btn-sm">Approve</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminDashboard",
  data() {
    return {
      users: [
        { id: 1, username: "JohnDoe", email: "john@example.com", role: "customer" },
        { id: 2, username: "JaneSmith", email: "jane@example.com", role: "professional" },
      ],
    };
  },
};
</script>
