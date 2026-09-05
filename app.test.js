const request = require('supertest');
const app = require('./app');

describe('GET /', () => {
  it('should respond with status 200 and display the student name', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toBe(200);
    expect(res.text).toContain('Gauresh Devendra Khot');
  });
});