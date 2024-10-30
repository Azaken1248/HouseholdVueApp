<template>
  <div class="container mt-5">
    <h2>Service Requests</h2>
    <form>
      <div class="mb-3">
        <label for="service" class="form-label">Service</label>
        <select id="service" class="form-select" required>
          <option value="plumbing">Plumbing</option>
          <option value="electrical">Electrical Repair</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="date" class="form-label">Date</label>
        <input type="date" class="form-control" id="date" required />
      </div>
      <button type="submit" class="btn btn-primary">Request Service</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "CustomerRequests",
};
</script>
